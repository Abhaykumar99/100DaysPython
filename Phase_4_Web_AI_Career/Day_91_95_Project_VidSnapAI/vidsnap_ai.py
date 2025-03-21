# ============================================================
# Day 91-95: Major Project — VidSnapAI (AI Video Tool Logic)
# ============================================================
# A Python backend for an AI video processing tool.
# pip install requests python-dotenv
# ============================================================

import os
import json
import time
from pathlib import Path
from datetime import datetime


class VideoProject:
    """Represents a single video generation project."""

    def __init__(self, title: str, script: str):
        self.project_id = f"vid_{int(time.time())}"
        self.title      = title
        self.script     = script
        self.created_at = datetime.now().isoformat()
        self.status     = "pending"
        self.scenes     = []
        self.output_url = None

    def to_dict(self):
        return self.__dict__


class ScriptAnalyzer:
    """Analyzes script and breaks it into scenes."""

    @staticmethod
    def split_into_scenes(script: str) -> list[dict]:
        """Split script text into logical scenes."""
        paragraphs = [p.strip() for p in script.split("\n\n") if p.strip()]
        scenes = []
        for i, para in enumerate(paragraphs, 1):
            words    = para.split()
            duration = max(3, len(words) // 3)   # ~3 words/second
            scenes.append({
                "scene_id"  : i,
                "text"      : para,
                "words"     : len(words),
                "duration"  : duration,
                "visual_cue": ScriptAnalyzer._generate_visual_cue(para),
            })
        return scenes

    @staticmethod
    def _generate_visual_cue(text: str) -> str:
        """Generate a visual description for the scene."""
        keywords = {
            "technology": "futuristic digital landscape",
            "nature"    : "lush green landscape, wide angle",
            "business"  : "modern office, professional setting",
            "space"     : "galaxy, stars, cosmos",
            "city"      : "urban skyline, busy streets",
        }
        for keyword, visual in keywords.items():
            if keyword.lower() in text.lower():
                return visual
        return "relevant background scene"


class ThumbnailGenerator:
    """Generates thumbnail metadata for each scene."""

    @staticmethod
    def create_thumbnail_prompt(scene: dict) -> str:
        """Create an image generation prompt for a scene thumbnail."""
        return (
            f"Cinematic, high quality image: {scene['visual_cue']}. "
            f"Professional video thumbnail style. "
            f"4K resolution, dramatic lighting."
        )


class VidSnapAI:
    """Main orchestrator class for the AI video generation pipeline."""

    PROJECTS_FILE = "vidsnap_projects.json"

    def __init__(self):
        self.projects: dict[str, VideoProject] = {}
        self.analyzer   = ScriptAnalyzer()
        self.thumbnailer = ThumbnailGenerator()
        self._load_projects()

    def create_project(self, title: str, script: str) -> VideoProject:
        """Create a new video project from a script."""
        project        = VideoProject(title, script)
        project.scenes = self.analyzer.split_into_scenes(script)
        project.status = "analyzed"

        print(f"\n✅ Project '{title}' created!")
        print(f"   ID     : {project.project_id}")
        print(f"   Scenes : {len(project.scenes)}")

        self.projects[project.project_id] = project
        self._save_projects()
        return project

    def generate_video(self, project_id: str) -> str:
        """Simulate video generation (would call AI API in production)."""
        project = self.projects.get(project_id)
        if not project:
            return "❌ Project not found."

        print(f"\n🎬 Generating video for: '{project.title}'")
        for i, scene in enumerate(project.scenes, 1):
            print(f"   Processing scene {i}/{len(project.scenes)}: {scene['text'][:40]}...")
            prompt = self.thumbnailer.create_thumbnail_prompt(scene)
            print(f"     Image prompt: {prompt[:60]}...")
            time.sleep(0.3)   # Simulate API call

        project.status     = "completed"
        project.output_url = f"https://vidsnap.ai/output/{project.project_id}.mp4"
        self._save_projects()

        return f"✅ Video ready: {project.output_url}"

    def get_project_summary(self, project_id: str):
        """Display a project's scene breakdown."""
        project = self.projects.get(project_id)
        if not project:
            print("❌ Project not found.")
            return

        total_duration = sum(s['duration'] for s in project.scenes)
        print(f"\n{'='*50}")
        print(f"📽  {project.title}")
        print(f"ID: {project.project_id} | Status: {project.status}")
        print(f"Total scenes: {len(project.scenes)} | Duration: ~{total_duration}s")
        print("=" * 50)
        for scene in project.scenes:
            print(f"\n  Scene {scene['scene_id']} ({scene['duration']}s)")
            print(f"  Text  : {scene['text'][:60]}...")
            print(f"  Visual: {scene['visual_cue']}")

    def _save_projects(self):
        data = {pid: p.to_dict() for pid, p in self.projects.items()}
        with open(self.PROJECTS_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def _load_projects(self):
        if Path(self.PROJECTS_FILE).exists():
            with open(self.PROJECTS_FILE) as f:
                data = json.load(f)
            # Reconstruct VideoProject objects
            for pid, d in data.items():
                p = VideoProject(d['title'], d['script'])
                p.__dict__.update(d)
                self.projects[pid] = p


# ============================================================
# DEMO
# ============================================================
if __name__ == "__main__":
    sample_script = """
    Artificial intelligence is transforming every industry today.
    From healthcare to finance, technology is enabling smarter decisions.

    In the business world, AI tools are helping companies automate repetitive tasks.
    Modern offices use machine learning to analyze data and improve productivity.

    The future of space exploration combines technology and human ingenuity.
    Scientists use AI to process galaxy images and discover new planets.

    As Python developers, we are at the forefront of this revolution.
    Learning Python opens doors to building the next generation of AI tools.
    """.strip()

    vidsnap = VidSnapAI()
    project = vidsnap.create_project("AI Revolution — A Short Film", sample_script)
    vidsnap.get_project_summary(project.project_id)

    result = vidsnap.generate_video(project.project_id)
    print(f"\n{result}")

    # Cleanup
    if Path("vidsnap_projects.json").exists():
        os.remove("vidsnap_projects.json")
