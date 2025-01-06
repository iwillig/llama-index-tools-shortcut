from llama_index.core.tools.tool_spec.base import BaseToolSpec
import logging
import requests
import os

logger = logging.getLogger(__name__)

def get_env_token():
    return os.getenv("SHORTCUT_API_TOKEN")

base_url = "https://api.app.shortcut.com/api/v3"

def prepare_headers(token):
    return {
        "Shortcut-Token": token,
        "Accept": "application/json; charset=utf-8",
        "Content-Type": "application/json",
        "User-Agent": "llama-tools-shortcut/0.0.1",
    }


class ShortcutToolSpec(BaseToolSpec):

    spec_functions = [
        "create_story"
    ]

    def __init__(self, shortcut_token):
        """"""
        self.shortcut_token = get_env_token()
        super().__init__()

    def create_story(self, story_name, workflow_state_id):
        url = f"{base_url}/stories/"
        response = requests.post(
            url,
            headers=prepare_headers(self.shortcut_token),
            json={"name": story_name,
                  "workflow_state_id": workflow_state_id}
        )
        response.raise_for_status()
        return response.json()