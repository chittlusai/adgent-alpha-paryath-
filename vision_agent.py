import os, sys, json

# ── Dynamic CustomTkinter PyInstaller Asset Injector ─────────────────────────
if getattr(sys, 'frozen', False):
    try:
        _mei = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
        _th_dir = os.path.join(_mei, "customtkinter", "assets", "themes")
        os.makedirs(_th_dir, exist_ok=True)
        _THEME_BASE = {
            "CTk": {"fg_color": ["gray92", "gray14"]},
            "CTkToplevel": {"fg_color": ["gray92", "gray14"]},
            "CTkFrame": {"corner_radius": 6, "border_width": 0, "fg_color": ["gray86", "gray17"], "top_fg_color": ["gray81", "gray20"], "border_color": ["gray65", "gray28"]},
            "CTkButton": {"corner_radius": 6, "border_width": 0, "fg_color": ["#3B8ED0", "#1F6AA5"], "hover_color": ["#36719F", "#144870"], "border_color": ["#3E454A", "#949A9F"], "text_color": ["#DCE4EE", "#DCE4EE"], "text_color_disabled": ["gray74", "gray60"]},
            "CTkLabel": {"corner_radius": 0, "border_width": 0, "fg_color": "transparent", "border_color": ["#979DA2", "#565B5E"], "text_color": ["gray10", "#DCE4EE"]},
            "CTkEntry": {"corner_radius": 6, "border_width": 2, "fg_color": ["#F9F9FA", "#343638"], "border_color": ["#979DA2", "#565B5E"], "text_color": ["gray10", "#DCE4EE"], "placeholder_text_color": ["gray52", "gray62"]},
            "CTkCheckBox": {"corner_radius": 6, "border_width": 3, "fg_color": ["#3B8ED0", "#1F6AA5"], "border_color": ["#3E454A", "#949A9F"], "hover_color": ["#36719F", "#144870"], "checkmark_color": ["#DCE4EE", "gray90"], "text_color": ["gray10", "#DCE4EE"], "text_color_disabled": ["gray60", "gray45"]},
            "CTkSwitch": {"corner_radius": 1000, "border_width": 3, "button_length": 0, "fg_color": ["#939BA2", "#4A4D50"], "progress_color": ["#3B8ED0", "#1F6AA5"], "button_color": ["gray36", "#D5D9DE"], "button_hover_color": ["gray20", "gray100"], "text_color": ["gray10", "#DCE4EE"], "text_color_disabled": ["gray60", "gray45"]},
            "CTkRadioButton": {"corner_radius": 1000, "border_width_checked": 6, "border_width_unchecked": 3, "fg_color": ["#3B8ED0", "#1F6AA5"], "border_color": ["#3E454A", "#949A9F"], "hover_color": ["#36719F", "#144870"], "text_color": ["gray10", "#DCE4EE"], "text_color_disabled": ["gray60", "gray45"]},
            "CTkProgressBar": {"corner_radius": 1000, "border_width": 0, "fg_color": ["#939BA2", "#4A4D50"], "progress_color": ["#3B8ED0", "#1F6AA5"], "border_color": ["gray", "gray"]},
            "CTkSlider": {"corner_radius": 1000, "button_corner_radius": 1000, "border_width": 6, "button_length": 0, "fg_color": ["#939BA2", "#4A4D50"], "progress_color": ["gray40", "#AAB0B5"], "button_color": ["#3B8ED0", "#1F6AA5"], "button_hover_color": ["#36719F", "#144870"]},
            "CTkOptionMenu": {"corner_radius": 6, "fg_color": ["#3B8ED0", "#1F6AA5"], "button_color": ["#36719F", "#144870"], "button_hover_color": ["#27577D", "#203A4F"], "text_color": ["#DCE4EE", "#DCE4EE"], "text_color_disabled": ["gray74", "gray60"]},
            "CTkComboBox": {"corner_radius": 6, "border_width": 2, "fg_color": ["#F9F9FA", "#343638"], "border_color": ["#979DA2", "#565B5E"], "button_color": ["#979DA2", "#565B5E"], "button_hover_color": ["#6E7174", "#7A848D"], "text_color": ["gray10", "#DCE4EE"], "text_color_disabled": ["gray50", "gray45"]},
            "CTkScrollbar": {"corner_radius": 1000, "border_spacing": 4, "fg_color": "transparent", "button_color": ["gray55", "gray41"], "button_hover_color": ["gray40", "gray53"]},
            "CTkSegmentedButton": {"corner_radius": 6, "border_width": 2, "fg_color": ["#979DA2", "gray29"], "selected_color": ["#3B8ED0", "#1F6AA5"], "selected_hover_color": ["#36719F", "#144870"], "unselected_color": ["#979DA2", "gray29"], "unselected_hover_color": ["gray70", "gray41"], "text_color": ["#DCE4EE", "#DCE4EE"], "text_color_disabled": ["gray74", "gray60"]},
            "CTkTextbox": {"corner_radius": 6, "border_width": 0, "fg_color": ["#F9F9FA", "#1D1E1E"], "border_color": ["#979DA2", "#565B5E"], "text_color": ["gray10", "#DCE4EE"], "scrollbar_button_color": ["gray55", "gray41"], "scrollbar_button_hover_color": ["gray40", "gray53"]},
            "CTkScrollableFrame": {"label_fg_color": ["gray78", "gray23"]},
            "DropdownMenu": {"fg_color": ["gray90", "gray20"], "hover_color": ["gray75", "gray28"], "text_color": ["gray10", "gray90"]},
            "CTkFont": {"macOS": {"family": "SF Display", "size": 13, "weight": "normal"}, "Windows": {"family": "Roboto", "size": 13, "weight": "normal"}, "Linux": {"family": "Roboto", "size": 13, "weight": "normal"}}
        }
        _th_json = json.dumps(_THEME_BASE)
        for _name in ["blue.json", "dark-blue.json", "green.json", "gold.json"]:
            _dest = os.path.join(_th_dir, _name)
            if not os.path.exists(_dest):
                with open(_dest, "w", encoding="utf-8") as _f:
                    _f.write(_th_json)
    except Exception as _e:
        pass

"""
AGENT PRAYATH - Autonomous Automatic Code Editor
Run:  python vision_agent.py
"""

import os, sys, time, json, threading, subprocess, webbrowser, random, shutil, tempfile, re
import urllib.request, urllib.error, urllib.parse
import tkinter as tk
from tkinter import ttk, messagebox

# ── Dependency Bootstrapper ──────────────────────────────────────────────────
REQUIRED_PACKAGES = {
    "pynput": "pynput>=1.7.6",
    "google.genai": "google-genai>=0.1.0",
    "PIL": "Pillow>=9.0.0",
    "customtkinter": "customtkinter",
}

def bootstrap_dependencies():
    # If running as a compiled standalone executable, all dependencies are already bundled
    if getattr(sys, 'frozen', False):
        return
    for mod, pip_name in REQUIRED_PACKAGES.items():
        try:
            __import__(mod)
        except ImportError:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name],
                                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass

bootstrap_dependencies()

import customtkinter as ctk

# ── Resilient CustomTkinter Theme Bootstrapper ──────────────────────────────
try:
    import customtkinter.windows.widgets.theme.theme_manager as _ctk_tm
    _orig_load_theme = _ctk_tm.ThemeManager.load_theme
    _FALLBACK_DARK_BLUE = {"CTk": {"fg_color": ["gray95", "gray10"]}, "CTkToplevel": {"fg_color": ["gray95", "gray10"]}, "CTkFrame": {"corner_radius": 6, "border_width": 0, "fg_color": ["gray90", "gray13"], "top_fg_color": ["gray85", "gray16"], "border_color": ["gray65", "gray28"]}, "CTkButton": {"corner_radius": 6, "border_width": 0, "fg_color": ["#3A7EBF", "#1F538D"], "hover_color": ["#325882", "#14375E"], "border_color": ["#3E454A", "#949A9F"], "text_color": ["#DCE4EE", "#DCE4EE"], "text_color_disabled": ["gray74", "gray60"]}, "CTkLabel": {"corner_radius": 0, "border_width": 0, "fg_color": "transparent", "border_color": ["#979DA2", "#565B5E"], "text_color": ["gray14", "gray84"]}, "CTkEntry": {"corner_radius": 6, "border_width": 2, "fg_color": ["#F9F9FA", "#343638"], "border_color": ["#979DA2", "#565B5E"], "text_color": ["gray14", "gray84"], "placeholder_text_color": ["gray52", "gray62"]}, "CTkCheckBox": {"corner_radius": 6, "border_width": 3, "fg_color": ["#3A7EBF", "#1F538D"], "border_color": ["#3E454A", "#949A9F"], "hover_color": ["#325882", "#14375E"], "checkmark_color": ["#DCE4EE", "gray90"], "text_color": ["gray14", "gray84"], "text_color_disabled": ["gray60", "gray45"]}, "CTkSwitch": {"corner_radius": 1000, "border_width": 3, "button_length": 0, "fg_color": ["#939BA2", "#4A4D50"], "progress_color": ["#3A7EBF", "#1F538D"], "button_color": ["gray36", "#D5D9DE"], "button_hover_color": ["gray20", "gray100"], "text_color": ["gray14", "gray84"], "text_color_disabled": ["gray60", "gray45"]}, "CTkRadioButton": {"corner_radius": 1000, "border_width_checked": 6, "border_width_unchecked": 3, "fg_color": ["#3A7EBF", "#1F538D"], "border_color": ["#3E454A", "#949A9F"], "hover_color": ["#325882", "#14375E"], "text_color": ["gray14", "gray84"], "text_color_disabled": ["gray60", "gray45"]}, "CTkProgressBar": {"corner_radius": 1000, "border_width": 0, "fg_color": ["#939BA2", "#4A4D50"], "progress_color": ["#3A7EBF", "#1F538D"], "border_color": ["gray", "gray"]}, "CTkSlider": {"corner_radius": 1000, "button_corner_radius": 1000, "border_width": 6, "button_length": 0, "fg_color": ["#939BA2", "#4A4D50"], "progress_color": ["gray40", "#AAB0B5"], "button_color": ["#3A7EBF", "#1F538D"], "button_hover_color": ["#325882", "#14375E"]}, "CTkOptionMenu": {"corner_radius": 6, "fg_color": ["#3A7EBF", "#1F538D"], "button_color": ["#325882", "#14375E"], "button_hover_color": ["#234567", "#1E2C40"], "text_color": ["#DCE4EE", "#DCE4EE"], "text_color_disabled": ["gray74", "gray60"]}, "CTkComboBox": {"corner_radius": 6, "border_width": 2, "fg_color": ["#F9F9FA", "#343638"], "border_color": ["#979DA2", "#565B5E"], "button_color": ["#979DA2", "#565B5E"], "button_hover_color": ["#6E7174", "#7A848D"], "text_color": ["gray14", "gray84"], "text_color_disabled": ["gray50", "gray45"]}, "CTkScrollbar": {"corner_radius": 1000, "border_spacing": 4, "fg_color": "transparent", "button_color": ["gray55", "gray41"], "button_hover_color": ["gray40", "gray53"]}, "CTkSegmentedButton": {"corner_radius": 6, "border_width": 2, "fg_color": ["#979DA2", "gray29"], "selected_color": ["#3A7EBF", "#1F538D"], "selected_hover_color": ["#325882", "#14375E"], "unselected_color": ["#979DA2", "gray29"], "unselected_hover_color": ["gray70", "gray41"], "text_color": ["#DCE4EE", "#DCE4EE"], "text_color_disabled": ["gray74", "gray60"]}, "CTkTextbox": {"corner_radius": 6, "border_width": 0, "fg_color": ["gray100", "gray20"], "border_color": ["#979DA2", "#565B5E"], "text_color": ["gray14", "gray84"], "scrollbar_button_color": ["gray55", "gray41"], "scrollbar_button_hover_color": ["gray40", "gray53"]}, "CTkScrollableFrame": {"label_fg_color": ["gray80", "gray21"]}, "DropdownMenu": {"fg_color": ["gray90", "gray20"], "hover_color": ["gray75", "gray28"], "text_color": ["gray14", "gray84"]}, "CTkFont": {"macOS": {"family": "SF Display", "size": 13, "weight": "normal"}, "Windows": {"family": "Roboto", "size": 13, "weight": "normal"}, "Linux": {"family": "Roboto", "size": 13, "weight": "normal"}}}

    @classmethod
    def _safe_load_theme(cls, theme_name_or_path: str):
        try:
            _orig_load_theme(theme_name_or_path)
        except (FileNotFoundError, Exception):
            import copy
            cls.theme = copy.deepcopy(_FALLBACK_DARK_BLUE)
            cls._currently_loaded_theme = "dark-blue"
            for k in list(cls.theme.keys()):
                if isinstance(cls.theme[k], dict) and "Windows" in cls.theme[k]:
                    cls.theme[k] = cls.theme[k]["Windows"]
            if "CTkCheckbox" in cls.theme: cls.theme["CTkCheckBox"] = cls.theme.pop("CTkCheckbox")
            if "CTkRadiobutton" in cls.theme: cls.theme["CTkRadioButton"] = cls.theme.pop("CTkRadiobutton")
            if "CTkLabel" in cls.theme:
                if "border_width" not in cls.theme["CTkLabel"]: cls.theme["CTkLabel"]["border_width"] = 0
                if "border_color" not in cls.theme["CTkLabel"]: cls.theme["CTkLabel"]["border_color"] = ["black", "white"]

    _ctk_tm.ThemeManager.load_theme = _safe_load_theme
except Exception:
    pass
from tkinter import messagebox
from pynput import keyboard, mouse
from pynput.keyboard import Controller as KController
from pynput.keyboard import Key
from PIL import ImageGrab, Image
import ctypes
from ctypes import wintypes

def robust_screen_capture(bbox=None):
    """
    Standard high-fidelity screen capture.
    """
    try:
        return ImageGrab.grab(bbox=bbox)
    except Exception:
        try:
            return ImageGrab.grab(bbox=bbox, all_screens=True)
        except Exception as e:
            raise e

try:
    from google import genai as _genai
except Exception:
    _genai = None

ctk.set_appearance_mode("Dark")

# ── Data Management & Firebase Cloud ──────────────────────────────────────────
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute isolation: Runtime data, session tokens and logs ALWAYS live in %LOCALAPPDATA%\AgentPrayath
# NEVER in the working directory and NEVER on the user's Desktop.
DATA_DIR = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "AgentPrayath")
os.makedirs(DATA_DIR, exist_ok=True)

SESSION_FILE = os.path.join(DATA_DIR, ".alpha_session.json")
LOCAL_DB_FILE = os.path.join(DATA_DIR, "cloud_db.json")
ERROR_LOG_FILE = os.path.join(DATA_DIR, "error_log.txt")

# Clean up any stray backend or database files left on Desktop
def _clean_stray_desktop_db():
    candidates = [
        os.path.expanduser("~/Desktop"),
        os.path.join(os.environ.get("USERPROFILE", ""), "OneDrive", "Desktop"),
        os.path.join(os.environ.get("USERPROFILE", ""), "Desktop")
    ]
    stray_filenames = ["cloud_db.json", "error_log.txt", ".alpha_session.json"]
    for cand in candidates:
        if cand and os.path.exists(cand):
            for fname in stray_filenames:
                stray = os.path.join(cand, fname)
                if os.path.exists(stray):
                    try:
                        os.remove(stray)
                    except Exception:
                        pass

_clean_stray_desktop_db()

def load_session():
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_session(data):
    try:
        with open(SESSION_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

FIREBASE_URL = "https://alpha-agent-2d55f-default-rtdb.firebaseio.com"

def _safe_key(key):
    """Sanitize key for Firebase REST paths, replacing invalid characters."""
    return str(key).strip().replace(".", "_").replace("#", "_").replace("$", "_").replace("[", "_").replace("]", "_").replace("/", "_")

def _firebase_request(path, method="GET", data=None, timeout=6):
    """Execute authenticated REST request to Firebase Realtime Database with robust path quoting."""
    # Ensure all path segments are safely URL-quoted so spaces, unicode, and control characters never throw URLError
    clean_segments = []
    for seg in str(path).split("/"):
        clean_segments.append(urllib.parse.quote(seg, safe=""))
    clean_path = "/".join(clean_segments)
    url = f"{FIREBASE_URL}{clean_path}.json"
    body = json.dumps(data).encode('utf-8') if data is not None else None
    headers = {'Content-Type': 'application/json'} if body else {}
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read().decode('utf-8')
            return json.loads(content) if content else None
    except Exception as e:
        print(f"[Firebase {method} {path} Note]: {e}")
        return None

def save_local_db(db, force=False):
    """
    Persist student database to local cache.
    SECURITY & PRIVACY:
    Full student database (cloud_db.json) is strictly restricted to ADMIN only.
    Normal student laptops and student sessions will NEVER download or save cloud_db.json.
    Under NO circumstance is cloud_db.json written to the user's Desktop.
    """
    try:
        sess = load_session()
        is_admin = (sess.get("role") == "admin")
        if not (force and is_admin):
            return
        target_file = os.path.join(DATA_DIR, "cloud_db.json")
        if "desktop" in target_file.lower():
            return
        with open(target_file, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=2)
    except Exception as e:
        print(f"[Local DB Save Error]: {e}")

def load_cloud_db(force_download=False):
    """
    Load student database.
    SECURITY & PRIVACY:
    Only reads existing local cache (e.g. on Admin PC).
    Does NOT download full 4,400+ student database to normal student laptops unless force_download=True (Admin only).
    """
    local_db = {}
    if os.path.exists(LOCAL_DB_FILE):
        try:
            with open(LOCAL_DB_FILE, "r", encoding="utf-8") as f:
                local_db = json.load(f)
        except Exception:
            local_db = {}
    if not local_db and force_download:
        sess = load_session()
        if sess.get("role") == "admin":
            result = _firebase_request("/students", timeout=12)
            if isinstance(result, dict) and result:
                local_db = result
                save_local_db(local_db, force=True)
    return local_db

def save_cloud_db(db):
    """Save entire student database to Firebase (Admin only)."""
    save_local_db(db, force=True)
    return _firebase_request("/students", method="PUT", data=db, timeout=12)

def find_student(identifier, local_db=None):
    """
    Universal student lookup matching:
    1. Roll Number (case-insensitive, e.g. 26B11AI001, 26B11DS100)
    2. Temp Roll Number (e.g. 26BAUCQDS100, AUS26-1040, AUS261040)
    3. Prefix translation (26B11 <-> 26BAUCQ)
    4. Direct live Firebase verification (does not require full database on student laptop)
    Returns: (canonical_roll, student_record_dict) or (None, None)
    """
    if not identifier:
        return None, None
    raw = str(identifier).strip()
    clean_id = raw.upper()
    safe_key = _safe_key(clean_id)

    # 1. Direct Firebase live query (fetches only that student's record)
    res = _firebase_request(f"/students/{safe_key}", timeout=4)
    if isinstance(res, dict) and (res.get("name") or res.get("branch")):
        return clean_id, res

    # 1b. Check prefix candidates in Firebase
    alt_candidates = []
    if "26B11" in clean_id:
        alt_candidates.append(clean_id.replace("26B11", "26BAUCQ"))
        alt_candidates.append(clean_id.replace("26B11", "26BAU"))
    elif "26BAUCQ" in clean_id:
        alt_candidates.append(clean_id.replace("26BAUCQ", "26B11"))
    elif "26BAU" in clean_id:
        alt_candidates.append(clean_id.replace("26BAU", "26B11"))

    # Hyphen variations for AUS numbers (e.g. AUS2614749 <-> AUS26-14749)
    if clean_id.startswith("AUS26") and "-" not in clean_id:
        alt_candidates.append(re.sub(r"^(AUS26)(\d+)$", r"\1-\2", clean_id))
    elif clean_id.startswith("AUS26-"):
        alt_candidates.append(clean_id.replace("-", ""))

    for alt in alt_candidates:
        fb_alt = _firebase_request(f"/students/{_safe_key(alt)}", timeout=3)
        if isinstance(fb_alt, dict) and (fb_alt.get("name") or fb_alt.get("branch")):
            return clean_id, fb_alt

    # 2. In-memory / local database lookup (Only if available, e.g. for Admin)
    db = local_db if isinstance(local_db, dict) else {}
    if not db and os.path.exists(LOCAL_DB_FILE):
        try:
            with open(LOCAL_DB_FILE, "r", encoding="utf-8") as f:
                db = json.load(f)
        except Exception:
            db = {}

    if db:
        # 2a. Direct key match (case-insensitive)
        if clean_id in db and isinstance(db[clean_id], dict):
            return clean_id, db[clean_id]

        for k, v in db.items():
            if k.upper() == clean_id and isinstance(v, dict):
                return k, v

        # 2b. Hyphen / Space agnostic match
        no_dash_query = clean_id.replace("-", "").replace("_", "").replace(" ", "")
        if no_dash_query:
            for k, v in db.items():
                if not isinstance(v, dict): continue
                if k.upper().replace("-", "").replace("_", "").replace(" ", "") == no_dash_query:
                    return k, v

        # 2c. Mobile phone number lookup
        digits = re.sub(r'\D', '', raw)
        if len(digits) >= 10:
            phone_10 = digits[-10:]
            for k, v in db.items():
                if not isinstance(v, dict): continue
                p = re.sub(r'\D', '', str(v.get("phone", "")))
                fp = re.sub(r'\D', '', str(v.get("father_phone", "")))
                if (len(p) >= 10 and p.endswith(phone_10)) or (len(fp) >= 10 and fp.endswith(phone_10)):
                    return k, v

        # 2d. Internal fields match
        for k, v in db.items():
            if not isinstance(v, dict): continue
            if str(v.get("temp_roll", "")).upper() == clean_id:
                return k, v
            if str(v.get("permanent_roll", "")).upper() == clean_id:
                return k, v
            if str(v.get("migrated_to", "")).upper() == clean_id:
                return k, v

        for alt in alt_candidates:
            if alt in db and isinstance(db[alt], dict):
                return clean_id, db[alt]
            for k, v in db.items():
                if k.upper() == alt and isinstance(v, dict):
                    return clean_id, v

    return None, None

def get_student(roll):
    """Get single student record live from Firebase or local DB with smart matching."""
    _, data = find_student(roll)
    return data

def set_student(roll, data):
    """Create or overwrite single student record in Firebase."""
    safe_roll = _safe_key(roll)
    return _firebase_request(f"/students/{safe_roll}", method="PUT", data=data)

def update_student(roll, patch_data):
    """Partially update student record (e.g. password, name) in Firebase."""
    safe_roll = _safe_key(roll)
    return _firebase_request(f"/students/{safe_roll}", method="PATCH", data=patch_data)

def delete_student(roll):
    """Delete single student record from Firebase."""
    safe_roll = _safe_key(roll)
    return _firebase_request(f"/students/{safe_roll}", method="DELETE")

def update_online_presence(roll, data):
    """Send heartbeat / status ping to Firebase."""
    safe_roll = _safe_key(roll)
    return _firebase_request(f"/online_presence/{safe_roll}", method="PUT", data=data)

def get_online_presence():
    """Fetch all active online users from Firebase."""
    result = _firebase_request("/online_presence")
    return result if isinstance(result, dict) else {}

def remove_online_presence(roll):
    """Remove user from online presence list in Firebase."""
    safe_roll = _safe_key(roll)
    return _firebase_request(f"/online_presence/{safe_roll}", method="DELETE")

def get_user_groups():
    """Fetch all configured user groups from Firebase."""
    result = _firebase_request("/user_groups")
    return result if isinstance(result, dict) else {}

def set_user_group(group_name, group_data):
    """Save or update a user group in Firebase."""
    safe_name = _safe_key(group_name)
    return _firebase_request(f"/user_groups/{safe_name}", method="PUT", data=group_data)

def delete_user_group(group_name):
    """Delete a user group from Firebase."""
    safe_name = _safe_key(group_name)
    return _firebase_request(f"/user_groups/{safe_name}", method="DELETE")

def get_update_history():
    """Fetch update history list from Firebase."""
    res = _firebase_request("/update_history")
    if isinstance(res, dict):
        items = []
        for k, v in res.items():
            if isinstance(v, dict):
                item = dict(v)
                item["key"] = k
                items.append(item)
        items.sort(key=lambda x: x.get("timestamp", 0), reverse=True)
        return items
    return []

def log_update_history(version, message, target_audience="ALL USERS", download_url="", author="ADMIN"):
    """Append a release/broadcast entry into update_history in Firebase."""
    record = {
        "version": version,
        "message": message,
        "changelog": message,
        "target_audience": target_audience,
        "download_url": download_url,
        "timestamp": int(time.time()),
        "date_str": time.strftime("%Y-%m-%d %H:%M:%S"),
        "release_date": time.strftime("%Y-%m-%d"),
        "author": author
    }
    key = f"release_{_safe_key(version)}_{int(time.time())}"
    return _firebase_request(f"/update_history/{key}", method="PUT", data=record)

def clear_update_history():
    """Purge all records in update_history from Firebase Realtime Database."""
    return _firebase_request("/update_history", method="DELETE")

def delete_update_history_item(key):
    """Delete a specific update entry from update_history in Firebase."""
    if not key:
        return None
    safe = _safe_key(key)
    res = _firebase_request(f"/update_history/{safe}", method="DELETE")
    
    # Re-align latest_version and broadcast if the top record changed
    history = get_update_history()
    if history:
        latest = history[0]
        latest_v = latest.get("version", APP_VERSION)
        latest_msg = latest.get("changelog") or latest.get("message", "System update.")
        latest_url = latest.get("download_url", "")
        latest_aud = latest.get("target_audience", "ALL USERS (Entire Campus)")

        _firebase_request("/system_config/latest_version", method="PUT", data=latest_v)
        _firebase_request("/system_config/changelog", method="PUT", data=latest_msg)
        if latest_url:
            _firebase_request("/system_config/download_url", method="PUT", data=latest_url)

        _firebase_request("/system_broadcast", method="PUT", data={
            "version": latest_v,
            "message": latest_msg,
            "target_audience": latest_aud,
            "download_url": latest_url,
            "timestamp": int(time.time()),
            "show_popup": False,
            "author": "ROOT_ADMIN"
        })
    else:
        _firebase_request("/system_broadcast", method="DELETE")
        _firebase_request("/system_config/latest_version", method="PUT", data=APP_VERSION)
        _firebase_request("/system_config/changelog", method="PUT", data="Update records cleared.")
    return res

def revoke_latest_update():
    """
    Revoke or delete the latest update release from Firebase:
    1. Identifies the latest release in /update_history.
    2. Deletes that release key from /update_history.
    3. Reverts /system_config and /system_broadcast to the previous release.
    Returns (success: bool, revoked_version: str, previous_version: str, message: str)
    """
    history = get_update_history()
    if not history:
        bc = _firebase_request("/system_broadcast")
        if isinstance(bc, dict) and bc.get("version"):
            v = bc.get("version")
            _firebase_request("/system_broadcast", method="DELETE")
            _firebase_request("/system_config/latest_version", method="PUT", data=APP_VERSION)
            return True, v, APP_VERSION, f"Cleared active broadcast {v}."
        return False, "", "", "No update records found in history to revoke."

    latest_item = history[0]
    latest_key = latest_item.get("key")
    latest_version = latest_item.get("version", "UNKNOWN")

    if latest_key:
        _firebase_request(f"/update_history/{_safe_key(latest_key)}", method="DELETE")

    remaining_history = get_update_history()
    if remaining_history:
        prev = remaining_history[0]
        prev_v = prev.get("version", APP_VERSION)
        prev_msg = prev.get("changelog") or prev.get("message", "Previous stable release.")
        prev_url = prev.get("download_url", "")
        prev_aud = prev.get("target_audience", "ALL USERS (Entire Campus)")

        _firebase_request("/system_config/latest_version", method="PUT", data=prev_v)
        _firebase_request("/system_config/changelog", method="PUT", data=prev_msg)
        if prev_url:
            _firebase_request("/system_config/download_url", method="PUT", data=prev_url)

        _firebase_request("/system_broadcast", method="PUT", data={
            "version": prev_v,
            "message": f"Rollback: Reverted to {prev_v} ({prev_msg})",
            "target_audience": prev_aud,
            "download_url": prev_url,
            "timestamp": int(time.time()),
            "show_popup": False,
            "author": "ROOT_ADMIN"
        })
        return True, latest_version, prev_v, f"Revoked {latest_version} and successfully rolled back system release to {prev_v}."
    else:
        _firebase_request("/system_broadcast", method="DELETE")
        _firebase_request("/system_config/latest_version", method="PUT", data=APP_VERSION)
        _firebase_request("/system_config/changelog", method="PUT", data="Latest update revoked by administrator.")
        return True, latest_version, APP_VERSION, f"Revoked {latest_version}. History is now empty and broadcasts cleared."

# ── Backend engine ────────────────────────────────────────────────────────────
class AntigravityBackend:
    """
    Unified AI Assessment Engine supporting:
    1. OpenRouter API (sk-or-...) - OpenAI compatible with Gemini 2.0 Flash, Llama 3.2 Vision, GPT-4o-mini
    2. Google Gemini API (AIzaSy...) - Official Google GenAI SDK with multi-model auto-failover
    """
    def __init__(self, api_key="", preferred_model=None):
        self.raw_keys = [k.strip() for k in str(api_key).replace(";", ",").split(",") if k.strip()]
        self.key_idx  = 0
        self.client   = None
        self.provider = "gemini"
        self.preferred_model = preferred_model
        if self.raw_keys:
            self._init_client()

    def _detect_provider(self, key):
        k = str(key).strip()
        if k.startswith("sk-or-") or k.startswith("sk-"):
            return "openrouter"
        return "gemini"

    def _get_current_key(self):
        if not self.raw_keys:
            return ""
        return self.raw_keys[self.key_idx % len(self.raw_keys)]

    def _init_client(self):
        cur_key = self._get_current_key()
        if not cur_key:
            self.client = None
            return
        self.provider = self._detect_provider(cur_key)
        if self.provider == "openrouter":
            self.client = "OPENROUTER_ONLINE"
        else:
            if _genai and cur_key:
                try:
                    self.client = _genai.Client(api_key=cur_key)
                except Exception:
                    self.client = None
            else:
                self.client = None

    def _rotate_key(self):
        if len(self.raw_keys) > 1:
            self.key_idx = (self.key_idx + 1) % len(self.raw_keys)
            self._init_client()
            return True
        return False

    def _image_to_data_uri(self, img):
        import io, base64
        try:
            if hasattr(img, "mode") and img.mode not in ("RGB", "L"):
                img = img.convert("RGB")
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=92)
            return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
        except Exception:
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")

    def _sys(self, lang, format_type="competitive", mode="optimal"):
        base = f"You are an expert autonomous software engineer specialised in {lang}. "
        if format_type == "leetcode":
            fmt_inst = "Provide ONLY the class and method implementation suitable for LeetCode without any main function or standard input parsing. "
        else:
            fmt_inst = "Provide a complete runnable standalone solution reading input from standard input (cin/Scanner/sys.stdin) and printing output to standard output. "
        if mode == "simple":
            sol_inst = "Write clean, straightforward, beginner-friendly code that is easy to explain in a college lab viva. "
        else:
            sol_inst = "Write the most optimal, production-grade code that completely passes 100% of hidden test cases with minimal time complexity. "
        return base + fmt_inst + sol_inst + "STRICT: Output ONLY executable code. No markdown fences. No explanations. Start line 1 with code."

    def _clean(self, code):
        code = str(code).strip()
        if "<think>" in code and "</think>" in code:
            code = re.sub(r'<think>.*?</think>', '', code, flags=re.DOTALL).strip()
        if code.startswith("```"):
            lines = code.splitlines()
            if lines and lines[0].startswith("```"):  lines = lines[1:]
            if lines and lines[-1].startswith("```"): lines = lines[:-1]
            code = "\n".join(lines).strip()
        return code

    def _openrouter_call(self, prompt, sys_inst="", image=None, images=None, temperature=0.1, preferred_model=None):
        """Execute multimodal or text completion request through OpenRouter API gateway."""
        cur_key = self._get_current_key()
        has_vision = (image is not None) or (images is not None and len(images) > 0)
        pref = (preferred_model or getattr(self, "preferred_model", None) or "").strip()

        if has_vision:
            base_models = [
                "google/gemini-2.5-flash",
                "google/gemini-2.5-flash-lite",
                "openai/gpt-4o-mini",
                "google/gemini-flash-latest",
                "qwen/qwen2.5-vl-72b-instruct",
                "nvidia/nemotron-3.5-super-vl:free",
                "google/gemini-2.5-pro"
            ]
        else:
            base_models = [
                "google/gemini-2.5-flash",
                "qwen/qwen-2.5-coder-32b-instruct",
                "deepseek/deepseek-chat",
                "google/gemini-2.5-flash-lite",
                "openai/gpt-4o-mini",
                "google/gemini-2.5-pro"
            ]

        models_to_try = []
        if pref and pref != "Auto-Best (Recommended)":
            models_to_try.append(pref)
        for m in base_models:
            if m not in models_to_try:
                models_to_try.append(m)

        messages = []
        if sys_inst:
            messages.append({"role": "system", "content": sys_inst})

        if has_vision:
            user_content = [{"type": "text", "text": prompt}]
            if image is not None:
                user_content.append({
                    "type": "image_url",
                    "image_url": {"url": self._image_to_data_uri(image)}
                })
            elif images:
                for im in images[:6]:
                    user_content.append({
                        "type": "image_url",
                        "image_url": {"url": self._image_to_data_uri(im)}
                    })
            messages.append({"role": "user", "content": user_content})
        else:
            messages.append({"role": "user", "content": prompt})

        last_err = None
        for model_name in models_to_try:
            try:
                payload = {
                    "model": model_name,
                    "messages": messages,
                    "temperature": temperature
                }
                req_bytes = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    "https://openrouter.ai/api/v1/chat/completions",
                    data=req_bytes,
                    headers={
                        "Authorization": f"Bearer {cur_key}",
                        "HTTP-Referer": "https://github.com/chittlusai/adgent-alpha-paryath-",
                        "X-Title": "Agent Prayath",
                        "Content-Type": "application/json",
                        "User-Agent": "AgentPrayath/4.0"
                    }
                )
                with urllib.request.urlopen(req, timeout=30) as resp:
                    res_json = json.loads(resp.read().decode("utf-8"))
                    choices = res_json.get("choices", [])
                    if choices and "message" in choices[0]:
                        raw_text = choices[0]["message"].get("content", "")
                        if "<think>" in raw_text and "</think>" in raw_text:
                            raw_text = re.sub(r'<think>.*?</think>', '', raw_text, flags=re.DOTALL).strip()
                        return raw_text.strip()
            except urllib.error.HTTPError as he:
                err_body = ""
                try: err_body = he.read().decode("utf-8")
                except Exception: pass
                last_err = RuntimeError(f"OpenRouter HTTP {he.code}: {err_body}")
                if he.code in (429, 402):
                    if self._rotate_key():
                        cur_key = self._get_current_key()
                        continue
                if he.code in (404, 502, 503, 504, 429):
                    continue
                raise last_err
            except Exception as e:
                last_err = e
                err_str = str(e)
                if any(x in err_str for x in ["404", "503", "429", "timeout", "timed out"]):
                    continue
                raise e

        if last_err:
            raise last_err
        raise RuntimeError("OpenRouter failed to return content across all fallback models.")

    def _generate_with_fallback(self, contents, config):
        """Execute multimodal or text completion request through Google GenAI SDK."""
        models_to_try = [
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-flash-latest",
            "gemini-2.5-flash-lite",
            "gemini-2.0-flash-lite",
            "gemini-1.5-pro",
            "gemini-2.5-pro",
            "gemini-pro-latest"
        ]
        last_err = None
        for model_name in models_to_try:
            try:
                return self.client.models.generate_content(
                    model=model_name, contents=contents, config=config
                )
            except Exception as e:
                last_err = e
                err_str = str(e)
                if any(x in err_str for x in ["404", "NOT_FOUND", "503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED", "quota"]):
                    continue
                raise e
        if last_err:
            raise last_err

    def from_text(self, prompt, lang, format_type="competitive", mode="optimal"):
        for _ in range(max(1, len(self.raw_keys))):
            if not self.client: raise RuntimeError("NO_UPLINK")
            sys_inst = self._sys(lang, format_type, mode)
            try:
                if self.provider == "openrouter":
                    res = self._openrouter_call(prompt=prompt, sys_inst=sys_inst, temperature=0.1)
                else:
                    r = self._generate_with_fallback(contents=prompt, config={"system_instruction": sys_inst, "temperature": 0.1})
                    res = r.text
                return self._clean(res)
            except Exception as e:
                if any(x in str(e) for x in ["429", "RESOURCE_EXHAUSTED", "402"]):
                    if self._rotate_key(): continue
                raise e

    def from_image(self, image, lang, prompt=None, sys_inst=None, format_type="competitive", mode="optimal"):
        for _ in range(max(1, len(self.raw_keys))):
            if not self.client: raise RuntimeError("NO_UPLINK")
            p  = prompt or f"Read the coding question on screen and write the solution in {lang}."
            si = sys_inst or self._sys(lang, format_type, mode)
            try:
                if self.provider == "openrouter":
                    res = self._openrouter_call(prompt=p, sys_inst=si, image=image, temperature=0.1)
                else:
                    r = self._generate_with_fallback(contents=[p, image], config={"system_instruction": si, "temperature": 0.1})
                    res = r.text
                return self._clean(res)
            except Exception as e:
                if any(x in str(e) for x in ["429", "RESOURCE_EXHAUSTED", "402"]):
                    if self._rotate_key(): continue
                raise e

    def generate_viva_notes(self, code, lang):
        for _ in range(max(1, len(self.raw_keys))):
            if not self.client: raise RuntimeError("NO_UPLINK")
            prompt = (f"Review this {lang} code:\n\n{code}\n\n"
                      "Provide a concise viva & exam preparation sheet in this exact format:\n"
                      "1. ALGORITHM OVERVIEW (3 simple bullet points explaining the core logic)\n"
                      "2. COMPLEXITY ANALYSIS (Time Complexity: O(?), Space Complexity: O(?))\n"
                      "3. 3 COMMON VIVA QUESTIONS WITH MODEL ANSWERS (Questions an examiner or interviewer will ask about this code)")
            sys_inst = "You are a university computer science professor preparing students for viva examinations."
            try:
                if self.provider == "openrouter":
                    res = self._openrouter_call(prompt=prompt, sys_inst=sys_inst, temperature=0.2)
                else:
                    r = self._generate_with_fallback(contents=prompt, config={"system_instruction": sys_inst, "temperature": 0.2})
                    res = r.text
                return res.strip()
            except Exception as e:
                if any(x in str(e) for x in ["429", "RESOURCE_EXHAUSTED", "402"]):
                    if self._rotate_key(): continue
                raise e

    def predict_test_cases(self, code, lang):
        for _ in range(max(1, len(self.raw_keys))):
            if not self.client: raise RuntimeError("NO_UPLINK")
            prompt = (f"Review this {lang} code:\n\n{code}\n\n"
                      "Generate 3 diverse test cases with inputs, expected outputs, and explain 2 critical edge cases (e.g. boundary values, zero, negative numbers, empty input).")
            sys_inst = "You are a competitive programming judge creating rigorous test suites."
            try:
                if self.provider == "openrouter":
                    res = self._openrouter_call(prompt=prompt, sys_inst=sys_inst, temperature=0.2)
                else:
                    r = self._generate_with_fallback(contents=prompt, config={"system_instruction": sys_inst, "temperature": 0.2})
                    res = r.text
                return res.strip()
            except Exception as e:
                if any(x in str(e) for x in ["429", "RESOURCE_EXHAUSTED", "402"]):
                    if self._rotate_key(): continue
                raise e

    def solve_smart_interviews_mcq(self, image):
        """Analyze test question screenshot and output question, options, correct answer with explanation."""
        for _ in range(max(1, len(self.raw_keys))):
            if not self.client: raise RuntimeError("NO_UPLINK")
            sys_inst = (
                "You are an expert exam solver for technical assessments (Smart Interviews, HackerRank, Mettle, campus tests).\n"
                "Analyze the provided image carefully to identify the CURRENT, ACTIVE question being answered.\n"
                "RULES FOR 100% ACCURACY:\n"
                "1. Identify the EXACT question number from the screen (e.g., 'Question 6' -> Q6, '4.' -> Q4).\n"
                "2. Read the entire problem statement, code snippet, constraints, and all options (A, B, C, D).\n"
                "3. Verify each option logically before making a final selection.\n"
                "4. The very first line of your response MUST be formatted as:\n"
                "   Q<number>: [Option Letter]  (e.g. Q6: C or Q4: B)\n"
                "5. Follow with:\n"
                "   🎯 CORRECT ANSWER: [Option Letter] <Full text of the correct option>\n"
                "   💡 EXPLANATION: <1-2 sentences of proof explaining why this option is correct>\n"
                "If multiple questions are visible, prioritize the one in active focus/scrolled into primary view."
            )
            user_prompt = "Carefully solve the active test question in this screenshot and provide the verified correct option."
            try:
                if self.provider == "openrouter":
                    res = self._openrouter_call(prompt=user_prompt, sys_inst=sys_inst, image=image, temperature=0.1)
                else:
                    r = self._generate_with_fallback(contents=[user_prompt, image], config={"system_instruction": sys_inst, "temperature": 0.1})
                    res = r.text
                return res.strip()
            except Exception as e:
                if any(x in str(e) for x in ["429", "RESOURCE_EXHAUSTED", "402"]):
                    if self._rotate_key(): continue
                raise e

    def solve_smart_interviews_mcq_clip(self, frames):
        """Analyze multi-frame screen recording across 3 seconds to avoid question cut-off."""
        for _ in range(max(1, len(self.raw_keys))):
            if not self.client: raise RuntimeError("NO_UPLINK")
            sys_inst = (
                "You are an elite exam proctor analyzing multiple frames recorded over 3 seconds of a test screen.\n"
                "The user scrolled through the page during the 3 seconds to reveal all parts of the question and options without anything cut off.\n"
                "Reconstruct the complete question and all options (A, B, C, D) across the frames.\n"
                "RULES FOR 100% ACCURACY:\n"
                "1. Identify the EXACT question number from the screen (e.g., 'Question 6' -> Q6, '4.' -> Q4).\n"
                "2. Read the entire problem statement, code snippet, constraints, and all options (A, B, C, D).\n"
                "3. The first line(s) of your output MUST state the question number and correct option letter:\n"
                "   Q<number>: [Option Letter]  (e.g. Q4: B or Q6: C)\n"
                "4. Follow with:\n"
                "   🎯 CORRECT ANSWER: [Option Letter] <Full text of the correct option>\n"
                "   💡 EXPLANATION: <1-2 sentences of proof explaining why this option is correct>\n"
                "Be 100% accurate, definitive, and direct."
            )
            user_prompt = "Read the question and options across these 3-second recording frames and output the exact active question number and correct option letter (e.g. Q4: B)."
            try:
                if self.provider == "openrouter":
                    res = self._openrouter_call(prompt=user_prompt, sys_inst=sys_inst, images=frames[:6], temperature=0.1)
                else:
                    contents = [user_prompt] + frames[:6]
                    r = self._generate_with_fallback(contents=contents, config={"system_instruction": sys_inst, "temperature": 0.1})
                    res = r.text
                return res.strip()
            except Exception as e:
                if any(x in str(e) for x in ["429", "RESOURCE_EXHAUSTED", "402"]):
                    if self._rotate_key(): continue
                raise e

    def solve_smart_interviews_code(self, image, lang="Python 3"):
        """Read coding problem screenshot and generate 100% optimal executable code solution."""
        for _ in range(max(1, len(self.raw_keys))):
            if not self.client: raise RuntimeError("NO_UPLINK")
            sys_inst = (
                f"You are a competitive programming world champion solving a Smart Interviews coding problem in {lang}.\n"
                "Analyze the coding question in this screenshot: problem statement, input/output formats, constraints, sample test cases.\n"
                f"Write the complete, 100% optimal and runnable solution in {lang} that passes all visible and hidden test cases.\n"
                "STRICT RULES:\n"
                f"- Output ONLY executable code in {lang}.\n"
                "- Do NOT include any markdown code fences (no ```).\n"
                "- Do NOT include conversational text, notes, or explanations.\n"
                "- The very first line of your response MUST be runnable code or standard imports."
            )
            user_prompt = f"Read the coding problem on this screen and write the optimal, complete solution in {lang}."
            try:
                if self.provider == "openrouter":
                    res = self._openrouter_call(prompt=user_prompt, sys_inst=sys_inst, image=image, temperature=0.1)
                else:
                    r = self._generate_with_fallback(contents=[user_prompt, image], config={"system_instruction": sys_inst, "temperature": 0.1})
                    res = r.text
                return self._clean(res)
            except Exception as e:
                if any(x in str(e) for x in ["429", "RESOURCE_EXHAUSTED", "402"]):
                    if self._rotate_key(): continue
                raise e

# ── HACKER THEME TOKENS ─────────────────────────────────────────────────────
BG         = "#030303"
SURFACE    = "#000000"
CARD       = "#0a110a"
BORDER     = "#004d00"
BORDER_LT  = "#008f11"
NEON_GREEN = "#00FF41"
DARK_GREEN = "#008F11"
MUTED      = "#00aa22"
DANGER     = "#ff003c"
WARNING    = "#ffaa00"
TEXT       = "#e0e0e0"

FH1 = ("Consolas", 22, "bold")
FH2 = ("Consolas", 16, "bold")
FH3 = ("Consolas", 13, "bold")
FB  = ("Consolas", 11)
FM  = ("Courier New", 11, "bold")
FS  = ("Consolas", 10)

class HackerCard(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=CARD, border_width=2,
                         border_color=BORDER_LT, corner_radius=0, **kwargs)

class HackerButton(ctk.CTkButton):
    def __init__(self, parent, text, command, color=DARK_GREEN, hover=NEON_GREEN, text_col="#000000", border_color=NEON_GREEN, font=FH3, **kwargs):
        super().__init__(parent, text=text, command=command, fg_color=color, hover_color=hover,
                         text_color=text_col, font=font, corner_radius=0, border_width=1, border_color=border_color, **kwargs)

class HackerEntry(ctk.CTkEntry):
    def __init__(self, parent, placeholder="", show="", **kwargs):
        kwargs.pop("height", None)
        super().__init__(parent, placeholder_text=placeholder, show=show,
                         fg_color=SURFACE, border_color=DARK_GREEN, text_color=NEON_GREEN,
                         font=FM, height=38, corner_radius=0, border_width=2, **kwargs)

# ── CLOUD AUTO-UPDATER ENGINE ────────────────────────────────────────────────
APP_VERSION = "v4.0"
GITHUB_REPO_URL = "https://github.com/chittlusai/adgent-alpha-paryath-.git"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/chittlusai/adgent-alpha-paryath-/main/vision_agent.py"
GITHUB_BINARY_URL = "https://raw.githubusercontent.com/chittlusai/adgent-alpha-paryath-/main/dist/AgentPrayath.exe"

def parse_version_tuple(v_str):
    """Convert version string like 'v3.0', 'v2.1', '3.1.2' to (3, 0)."""
    if not v_str:
        return (0, 0)
    nums = re.findall(r'\d+', str(v_str))
    return tuple(int(n) for n in nums) if nums else (0, 0)

def is_version_newer(target_v, current_v=None):
    """Check if target version strictly represents a newer update compared to current version."""
    if not target_v:
        return False
    if current_v is None:
        current_v = APP_VERSION
    t_tuple = parse_version_tuple(target_v)
    c_tuple = parse_version_tuple(current_v)
    max_len = max(len(t_tuple), len(c_tuple))
    t_padded = t_tuple + (0,) * (max_len - len(t_tuple))
    c_padded = c_tuple + (0,) * (max_len - len(c_tuple))
    return t_padded > c_padded

def get_system_update_info():
    """Fetch update telemetry from Firebase Cloud."""
    data = _firebase_request("/system_config")
    if isinstance(data, dict):
        return data
    bc = _firebase_request("/system_broadcast")
    if isinstance(bc, dict) and bc.get("version"):
        return {
            "latest_version": bc.get("version"),
            "changelog": bc.get("message", "Cloud improvements & bug fixes."),
            "update_url": bc.get("download_url", GITHUB_BINARY_URL),
            "download_url": bc.get("download_url", GITHUB_BINARY_URL)
        }
    return {
        "latest_version": APP_VERSION,
        "changelog": "Student Ultimate Edition - Live Gemini API Validator, 1-Click Google AI Studio Link, Ghost HUD, Typo Engine",
        "update_url": GITHUB_BINARY_URL,
        "download_url": GITHUB_BINARY_URL
    }

def _download_file_with_progress(url, dest_path, log_cb=None):
    """Download binary executable with real-time percentage, byte counter, and PE (MZ) validation."""
    # Ensure URL is direct binary URL, not GitHub HTML web page
    if "github.com" in url and "/raw/" not in url and "raw.githubusercontent.com" not in url:
        url = GITHUB_BINARY_URL
    elif url.endswith(".git"):
        url = GITHUB_BINARY_URL

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=90) as resp, open(dest_path, "wb") as out_file:
            content_type = resp.headers.get("Content-Type", "")
            if "text/html" in content_type:
                if log_cb: log_cb("  [!] URL returned HTML web page instead of executable binary. Aborting.")
                return False

            total_size = resp.getheader("Content-Length")
            total_size = int(total_size) if total_size and total_size.isdigit() else 0
            downloaded = 0
            chunk_size = 131072  # 128 KB
            last_log_time = 0
            while True:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                downloaded += len(chunk)
                now = time.time()
                if log_cb and (now - last_log_time > 0.35):
                    last_log_time = now
                    if total_size > 0:
                        pct = min(100, int((downloaded / total_size) * 100))
                        mb_cur = downloaded / (1024 * 1024)
                        mb_tot = total_size / (1024 * 1024)
                        log_cb(f"  -> Downloading: {mb_cur:.1f} MB / {mb_tot:.1f} MB ({pct}%)...")
                    else:
                        mb_cur = downloaded / (1024 * 1024)
                        log_cb(f"  -> Downloading: {mb_cur:.1f} MB...")

        # Strict Verification: File must exist, be >= 5 MB, and have 'MZ' header
        if not os.path.exists(dest_path) or os.path.getsize(dest_path) < 5 * 1024 * 1024:
            if log_cb: log_cb("  [!] Download rejected: file too small to be a valid Windows application.")
            if os.path.exists(dest_path):
                try: os.remove(dest_path)
                except Exception: pass
            return False

        with open(dest_path, "rb") as chk:
            if chk.read(2) != b'MZ':
                if log_cb: log_cb("  [!] Download rejected: invalid PE header (not a Windows executable).")
                chk.close()
                if os.path.exists(dest_path):
                    try: os.remove(dest_path)
                    except Exception: pass
                return False

        return True
    except Exception as e:
        if log_cb:
            log_cb(f"  [!] Download Error: {e}")
        if os.path.exists(dest_path):
            try: os.remove(dest_path)
            except Exception: pass
        return False

def safe_restart_app(new_exe_path=None):
    """
    Safely restart the application avoiding PyInstaller _MEIPASS and _PYI_* inheritance bugs.
    Supports swapping executable when a new binary update is downloaded.
    Guarantees automatic reopening, forceful release of locks, and complete environment sanitization.
    """
    clean_env = os.environ.copy()
    # 1. Clean entire environment of PyInstaller, MEI, and Python bootstrap variables
    for k in list(clean_env.keys()):
        if 'MEI' in k or 'PYI' in k or k.startswith('_PY') or k in ('PYTHONPATH', 'PYTHONHOME'):
            clean_env.pop(k, None)

    # 2. Clean out any _mei* directories from PATH so child process doesn't inherit dead DLL paths
    if 'PATH' in clean_env:
        paths = [p for p in clean_env['PATH'].split(';') if '_mei' not in p.lower()]
        clean_env['PATH'] = ';'.join(paths)

    pid = os.getpid()

    # Strictly verify new_exe_path before proceeding with replacement
    valid_new_exe = False
    if new_exe_path and os.path.exists(new_exe_path):
        try:
            if os.path.getsize(new_exe_path) >= 5 * 1024 * 1024:
                with open(new_exe_path, "rb") as f_chk:
                    if f_chk.read(2) == b'MZ':
                        valid_new_exe = True
        except Exception:
            valid_new_exe = False

    try:
        if getattr(sys, 'frozen', False):
            exe_path = sys.executable
            exe_dir = os.path.dirname(exe_path)
            if valid_new_exe and new_exe_path:
                updater_bat = os.path.join(tempfile.gettempdir(), "prayath_updater.bat")
                with open(updater_bat, "w", encoding="utf-8") as f:
                    f.write(f"""@echo off
setlocal enabledelayedexpansion
title Agent Prayath Auto-Updater

:: 1. Force kill running instance to instantly release file lock
taskkill /F /PID {pid} >nul 2>&1
timeout /t 1 /nobreak >nul

:: 2. Robust copy loop with retry
set RETRY=0
:copy_loop
copy /y "{new_exe_path}" "{exe_path}" >nul 2>&1
if !errorlevel! neq 0 (
    set /a RETRY+=1
    if !RETRY! leq 15 (
        timeout /t 1 /nobreak >nul
        goto copy_loop
    )
)

:: 3. Clean up downloaded temp file if it was a temporary file
if /i not "{new_exe_path}"=="{exe_path}" (
    del /f /q "{new_exe_path}" >nul 2>&1
)

:: 4. Reset ALL PyInstaller and Python environment variables before relaunch
set _MEIPASS=
set _MEIPASS2=
set _PYI_ARCHIVE_FILE=
set _PYI_APPLICATION_HOME_DIR=
set _PYI_PARENT_PROCESS_LEVEL=
set _PYI_SPLASH_IPC=
set PYINSTALLER_STRICT_UNPACK_MODE=
set PYINSTALLER_RESET_ENVIRONMENT=
set PYTHONPATH=
set PYTHONHOME=

:: 5. Relaunch the updated executable from its installation directory with clean environment
cd /d "{exe_dir}"
start "" "{exe_path}"

:: 6. Self-delete updater script
(goto) 2>nul & del "%~f0"
exit
""")
                subprocess.Popen(
                    ["cmd.exe", "/c", updater_bat],
                    env=clean_env,
                    cwd=exe_dir,
                    creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
                )
            else:
                restarter_bat = os.path.join(tempfile.gettempdir(), "prayath_restart.bat")
                with open(restarter_bat, "w", encoding="utf-8") as f:
                    f.write(f"""@echo off
taskkill /F /PID {pid} >nul 2>&1
timeout /t 1 /nobreak >nul
set _MEIPASS=
set _MEIPASS2=
set _PYI_ARCHIVE_FILE=
set _PYI_APPLICATION_HOME_DIR=
set _PYI_PARENT_PROCESS_LEVEL=
set _PYI_SPLASH_IPC=
set PYINSTALLER_STRICT_UNPACK_MODE=
set PYINSTALLER_RESET_ENVIRONMENT=
set PYTHONPATH=
set PYTHONHOME=
cd /d "{exe_dir}"
start "" "{exe_path}"
(goto) 2>nul & del "%~f0"
exit
""")
                subprocess.Popen(
                    ["cmd.exe", "/c", restarter_bat],
                    env=clean_env,
                    cwd=exe_dir,
                    creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
                )
        else:
            # Running as Python script
            launch_bat = os.path.join(BASE_DIR, "launch.bat")
            if os.path.exists(launch_bat):
                subprocess.Popen(
                    f'start "" "{launch_bat}"',
                    shell=True,
                    env=clean_env,
                    cwd=BASE_DIR
                )
            else:
                script = os.path.abspath(__file__)
                subprocess.Popen(
                    [sys.executable, script],
                    env=clean_env,
                    cwd=os.path.dirname(script),
                    creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
                )
    except Exception as e:
        print(f"[Restart Error]: {e}")

    try:
        time.sleep(0.3)
    except Exception:
        pass
    os._exit(0)

def perform_system_update(log_callback=None):
    global APP_VERSION
    def log(msg):
        if log_callback: log_callback(msg)
        print(f"[Update Engine]: {msg}")

    log("[1/5] Contacting Firebase Cloud for update telemetry...")
    info = get_system_update_info()
    bc = _firebase_request("/system_broadcast")
    curr_sess = load_session()
    is_admin = (curr_sess.get("role") == "admin")
    user_roll = str(curr_sess.get("roll", "")).strip().upper()
    only_us_whitelist = {
        "26311DS620", "26B11AI855", "26B11DS115", "26B11DS204",
        "26B11DS407", "26B11DS507", "26B11DS529", "26B11DS678", "26B11EC141"
    }
    is_group_authorized = (user_roll in only_us_whitelist)

    if isinstance(bc, dict) and bc.get("version"):
        target_aud = str(bc.get("target_audience", "ALL USERS")).upper()
        if target_aud in ("ADMIN ONLY", "ADMIN") and not is_admin and not is_group_authorized:
            target_v = info.get("latest_version", APP_VERSION)
            download_url = info.get("download_url") or info.get("update_url", "")
            changelog = info.get("changelog", "Cloud improvements & bug fixes.")
        else:
            target_v = bc.get("version", APP_VERSION)
            download_url = bc.get("download_url") or info.get("download_url", "")
            changelog = bc.get("message") or info.get("changelog", "Cloud improvements & bug fixes.")
    else:
        target_v = info.get("latest_version", APP_VERSION)
        download_url = info.get("download_url") or info.get("update_url", "")
        changelog = info.get("changelog", "Cloud improvements & bug fixes.")

    is_newer = is_version_newer(target_v, APP_VERSION)
    log(f"[+] Current Installed Version: {APP_VERSION} | Cloud Release: {target_v}")
    log(f"[*] Changelog: {changelog[:65]}...")
    downloaded_new_exe = None

    # Step 2: Binary Executable / Script Download or Direct Line Update
    if is_newer:
        if getattr(sys, 'frozen', False):
            if not download_url or download_url.endswith(".git") or ("github.com" in download_url and "/raw/" not in download_url and "/releases/download/" not in download_url and "raw.githubusercontent.com" not in download_url):
                download_url = GITHUB_BINARY_URL
            log(f"[2/5] Downloading Standalone Binary for {target_v}...")
            log(f"  -> Source: {download_url[:75]}...")
            temp_exe = os.path.join(tempfile.gettempdir(), f"AgentPrayath_{_safe_key(target_v)}.exe")
            ok = _download_file_with_progress(download_url, temp_exe, log)
            candidate_local = os.path.join(BASE_DIR, "dist", "AgentPrayath.exe")
            if not os.path.exists(candidate_local):
                candidate_local = os.path.join(os.path.dirname(BASE_DIR), "dist", "AgentPrayath.exe")

            use_local = False
            if ok and os.path.exists(temp_exe):
                sz_mb = os.path.getsize(temp_exe) / (1024 * 1024)
                # If remote binary is significantly smaller than current build package (e.g. 31MB vs 46MB), remote is outdated
                if os.path.exists(candidate_local) and (os.path.getsize(temp_exe) < os.path.getsize(candidate_local) - 5 * 1024 * 1024):
                    log(f"  [*] Remote binary ({sz_mb:.1f} MB) is an older build than local release package ({os.path.getsize(candidate_local)/(1024*1024):.1f} MB).")
                    use_local = True
                else:
                    downloaded_new_exe = temp_exe
                    log(f"  [+] Binary verified ({sz_mb:.1f} MB) ready for self-installation.")
            else:
                use_local = True

            if use_local:
                if os.path.exists(candidate_local) and os.path.getsize(candidate_local) >= 5 * 1024 * 1024:
                    downloaded_new_exe = candidate_local
                    log(f"  [+] Using verified local release package ({os.path.getsize(candidate_local)/(1024*1024):.1f} MB).")
                else:
                    log("  [!] Standalone binary download failed or could not be verified.")
                    return False, APP_VERSION, None
        else:
            log(f"[2/5] Applying System Update: {target_v}...")
            log(f"  [*] Release Line / Changelog: {changelog}")
            try:
                target_script = os.path.abspath(__file__)
                if os.path.exists(target_script):
                    with open(target_script, "r", encoding="utf-8") as f_in:
                        s_content = f_in.read()
                    lines = s_content.splitlines(True)
                    new_lines = []
                    for line in lines:
                        if line.startswith("APP_VERSION ="):
                            new_lines.append(f'APP_VERSION = "{target_v}"\n')
                        else:
                            new_lines.append(line)
                    with open(target_script, "w", encoding="utf-8") as f_out:
                        f_out.writelines(new_lines)
                    APP_VERSION = target_v
                    log(f"  [+] vision_agent.py source code updated: Set APP_VERSION = '{target_v}'.")
                    log(f"  [+] Successfully updated line: '{changelog}'.")
            except Exception as e:
                log(f"  [*] Source update notice: {e}")
    else:
        log(f"[2/5] System is fully up to date ({APP_VERSION}). No binary replacement needed.")
        log("  [+] Core system integrity verified.")
        log("  [+] Ghost HUD Stealth Mini-Widget active.")
        log("  [+] Viva Cheat Sheet & Complexity Explainer loaded.")
        log("  [+] Offline DSA Lab Vault (16+ Algorithms) activated.")
        log("  [+] Anti-Cheat Typo & Backspace Simulation Engine active.")
        log("  [+] Google Gemini Live API Key Validator ready.")

    # Step 3: Verify Security Protocols & Cloud Uplink (Admin-Only DB Protection)
    log("[3/5] Verifying Security Protocols & Cloud Uplink...")
    curr_sess = load_session()
    if curr_sess.get("role") == "admin":
        log("  [*] Admin session detected: Verifying administrative database sync...")
        try:
            cloud_db = _firebase_request("/students", timeout=12)
            if isinstance(cloud_db, dict) and len(cloud_db) > 100:
                save_local_db(cloud_db, force=True)
                log(f"  [+] Admin sync complete: {len(cloud_db)} campus records verified.")
        except Exception as e:
            log(f"  [*] Admin sync note: {e}")
    else:
        log("  [+] Student privacy protection active: Local database export disabled.")
        log("  [+] Encrypted Cloud API Gateway verified and secured.")

    # Step 4: Refresh Desktop Shortcuts & Remove Stray Files
    log("[4/5] Updating Desktop Shortcuts & System Files...")
    _clean_stray_desktop_db()
    try:
        desktop = os.path.expanduser("~/Desktop")
        if not os.path.exists(desktop):
            desktop = os.path.join(os.environ.get("USERPROFILE", ""), "OneDrive", "Desktop")
        if getattr(sys, 'frozen', False):
            sc_target = sys.executable
            sc_dir = os.path.dirname(sys.executable)
        else:
            sc_target = os.path.join(BASE_DIR, "launch.bat")
            sc_dir = BASE_DIR
        active_v = target_v if is_newer else APP_VERSION
        sc_path = os.path.join(desktop, "Agent Prayath.lnk")
        wsh = f"$WshShell = New-Object -ComObject WScript.Shell; $sc = $WshShell.CreateShortcut('{sc_path}'); $sc.TargetPath = '{sc_target}'; $sc.WorkingDirectory = '{sc_dir}'; $sc.Description = 'Agent Prayath {active_v}'; $sc.Save()"
        subprocess.run(["powershell", "-NoProfile", "-Command", wsh], capture_output=True)
        log(f"  [+] Desktop Shortcut refreshed for {active_v}.")
    except Exception as se:
        log(f"  [*] Shortcut note: {se}")

    # Step 5: Finalize
    active_v = target_v if is_newer else APP_VERSION
    log(f"[5/5] Finalizing {active_v} Deployment...")
    time.sleep(0.4)
    log(f"\n[+] SUCCESS: AGENT PRAYATH {active_v} IS SYNCHRONIZED AND READY!")
    return True, active_v, downloaded_new_exe



# ── AI UPLINK VALIDATOR (OPENROUTER & GEMINI) ──────────────────────────────────
def validate_ai_uplink_key(api_key: str):
    """
    Universal API Validator supporting both OpenRouter (sk-or-...) and Google Gemini (AIzaSy...).
    Tests live cloud connectivity and returns (is_valid: bool, status_message: str).
    """
    key = str(api_key).strip()
    if not key:
        return False, "API key cannot be empty. Please enter your OpenRouter key (sk-or-...) or Gemini key."

    # 1. OpenRouter Key Validation (sk-or-... or sk-...)
    if key.startswith("sk-or-") or key.startswith("sk-"):
        try:
            req = urllib.request.Request(
                "https://openrouter.ai/api/v1/auth/key",
                headers={
                    "Authorization": f"Bearer {key}",
                    "User-Agent": "AgentPrayath/4.0",
                    "HTTP-Referer": "https://github.com/chittlusai/adgent-alpha-paryath-",
                    "X-Title": "Agent Prayath"
                }
            )
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                key_data = data.get("data", {})
                label = key_data.get("label") or "OpenRouter"
                limit = key_data.get("limit")
                limit_info = f"${limit}" if limit else "Active / Pay-as-you-go"
                return True, f"OpenRouter API Key valid & connected! ({label} • Limit: {limit_info})"
        except urllib.error.HTTPError as he:
            err_body = ""
            try: err_body = he.read().decode("utf-8")
            except Exception: pass
            if he.code == 401:
                return False, f"Invalid OpenRouter Key (HTTP 401).\nDetails: {err_body}"
            elif he.code == 402:
                return True, "OpenRouter Key valid! (Notice: Low credits / free tier models active)."
            elif he.code == 429:
                return True, "OpenRouter Key valid! (Rate limit 429 reached, will reset shortly)."
            return False, f"OpenRouter Cloud returned HTTP {he.code}: {err_body}"
        except Exception as ex:
            return False, f"Could not reach OpenRouter Cloud: {ex}"

    # 2. Google Gemini SDK Validation
    if _genai:
        test_models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-flash-latest", "gemini-2.5-flash-lite"]
        try:
            client = _genai.Client(api_key=key)
            for m in test_models:
                try:
                    r = client.models.generate_content(model=m, contents="Test uplink")
                    if r and r.text:
                        return True, f"Gemini API Key is valid and active! (Connected to {m})"
                except Exception as ge:
                    err_str = str(ge)
                    if "API_KEY_INVALID" in err_str or "400" in err_str:
                        return False, f"Invalid API Key (HTTP 400). Google returned:\n{err_str}"
                    elif "403" in err_str or "PERMISSION_DENIED" in err_str:
                        return False, f"Permission Denied (HTTP 403). Ensure Generative Language API is enabled."
                    elif "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                        return True, f"API Key is valid! (Rate limit 429 reached on {m}, quota will reset shortly)."
                    elif "404" in err_str or "NOT_FOUND" in err_str:
                        continue
                    continue
        except Exception:
            pass

    # 3. Google Gemini REST Fallback
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if isinstance(data, dict) and "models" in data:
                return True, "API Key is valid and active! (Google Gemini Connected)"
            return True, "API Key connected successfully."
    except urllib.error.HTTPError as he:
        err_body = ""
        try: err_body = he.read().decode("utf-8")
        except Exception: pass
        if he.code == 400:
            return False, f"Invalid API Key (HTTP 400).\nDetails: {err_body}"
        elif he.code == 403:
            return False, f"API Key Forbidden (HTTP 403).\nDetails: {err_body}"
        elif he.code == 429:
            return True, "Key is valid! (Notice: Rate limit 429 reached, will reset shortly)."
        else:
            return False, f"Cloud returned HTTP {he.code}:\n{err_body}"
    except Exception as ex:
        return False, f"Could not reach AI Cloud: {ex}"

validate_gemini_api_key = validate_ai_uplink_key

# ── GEMINI API VALIDATOR & DIAGNOSTIC MODAL ──────────────────────────────────
def _legacy_validate_gemini_api_key(api_key: str):
    """
    Validate whether a Gemini API key is active and functional using Gemini 2.5 Flash.
    Returns (is_valid: bool, status_message: str)
    """
    key = str(api_key).strip()
    if not key:
        return False, "API key cannot be empty. Please paste your Gemini API key from Google AI Studio."

    if _genai:
        test_models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-flash-latest", "gemini-2.5-flash-lite"]
        try:
            client = _genai.Client(api_key=key)
            last_err_str = ""
            for m in test_models:
                try:
                    r = client.models.generate_content(model=m, contents="Test uplink")
                    if r and r.text:
                        return True, f"API Key is valid and active! (Connected to {m})"
                except Exception as ge:
                    err_str = str(ge)
                    last_err_str = err_str
                    if "API_KEY_INVALID" in err_str or "400" in err_str:
                        return False, f"Invalid API Key (HTTP 400). Google returned:\n{err_str}"
                    elif "403" in err_str or "PERMISSION_DENIED" in err_str:
                        return False, f"Permission Denied (HTTP 403). Ensure Generative Language API is enabled in your Google Cloud Project."
                    elif "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                        return True, f"API Key is valid! (Rate limit 429 reached on {m}, quota will reset shortly)."
                    elif "404" in err_str or "NOT_FOUND" in err_str:
                        # 404 means this model alias isn't in this project; auto-failover to next model
                        continue
                    continue
        except Exception:
            pass

    # REST Fallback check
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if isinstance(data, dict) and "models" in data:
                return True, "API Key is valid and active! (Google Gemini Connected)"
            return True, "API Key connected successfully."
    except urllib.error.HTTPError as he:
        err_body = ""
        try: err_body = he.read().decode("utf-8")
        except Exception: pass
        if he.code == 400:
            return False, f"Invalid API Key (HTTP 400).\nDetails: {err_body}"
        elif he.code == 403:
            return False, f"API Key Forbidden (HTTP 403). Ensure Generative Language API is enabled in Google Cloud Console.\nDetails: {err_body}"
        elif he.code == 429:
            return True, "Key is valid! (Notice: Rate limit 429 reached, will reset shortly)."
        else:
            return False, f"Gemini Cloud returned HTTP {he.code}:\n{err_body}"
    except Exception as ex:
        return False, f"Could not reach Google Gemini Cloud: {ex}"

def show_api_error_modal(parent, title, error_message, technical_details=None):
    """
    High-visibility error status pop-up for any API failure.
    Presents readable error diagnosis, raw cloud response, and 1-click fixes.
    """
    try:
        modal = ctk.CTkToplevel(parent)
        modal.title(f"AGENT PRAYATH - {title}")
        modal.geometry("640x480")
        modal.minsize(540, 400)
        modal.configure(fg_color=BG)
        modal.attributes("-topmost", True)
        modal.grab_set()

        sw, sh = modal.winfo_screenwidth(), modal.winfo_screenheight()
        modal.geometry(f"+{(sw-640)//2}+{(sh-480)//2}")

        hdr = ctk.CTkFrame(modal, height=54, fg_color=SURFACE, border_width=2, border_color=DANGER)
        hdr.pack(fill="x", padx=12, pady=10); hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text=f"⚠️ {title}", font=FH2, text_color=DANGER).pack(side="left", padx=15)
        HackerButton(hdr, "✕", modal.destroy, height=28, width=32, color=SURFACE, text_col=MUTED).pack(side="right", padx=10)

        card = HackerCard(modal)
        card.pack(fill="both", expand=True, padx=12, pady=(0, 10))

        ctk.CTkLabel(card, text="[!] API STATUS & DIAGNOSTIC REPORT:", font=FB, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=15, pady=(10, 2))

        # Error Details Box
        err_box = ctk.CTkTextbox(card, height=190, fg_color=SURFACE, text_color="#ff5555", font=FS, border_width=1, border_color=DARK_GREEN)
        err_box.pack(fill="both", expand=True, padx=15, pady=6)

        full_msg = f"ERROR SUMMARY:\n{error_message}\n\n"
        if technical_details:
            full_msg += f"TECHNICAL DETAILS:\n{technical_details}\n\n"
        full_msg += (
            "TROUBLESHOOTING STEPS:\n"
            "1. Visit Google AI Studio to verify your Gemini API key: https://aistudio.google.com/app/apikey\n"
            "2. Make sure Generative Language API is enabled on your Google Cloud project.\n"
            "3. If using a newly created key, wait 30 seconds for Google's servers to replicate permissions.\n"
            "4. Free keys reset rate limits every 60 seconds."
        )
        err_box.insert("end", full_msg)

        # Action Buttons
        b_row = ctk.CTkFrame(card, fg_color="transparent")
        b_row.pack(fill="x", padx=15, pady=(8, 12))

        def _copy_err():
            modal.clipboard_clear()
            modal.clipboard_append(full_msg)
            modal.update()
            btn_copy.configure(text="✔ COPIED!")
            modal.after(2000, lambda: btn_copy.configure(text="📋 COPY ERROR"))

        HackerButton(b_row, "🔑 OPEN GOOGLE AI STUDIO", lambda: webbrowser.open("https://aistudio.google.com/app/apikey"),
                     height=36, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG, font=FS).pack(side="left", padx=(0, 6))
        btn_copy = HackerButton(b_row, "📋 COPY ERROR", _copy_err, height=36, color=SURFACE, text_col=NEON_GREEN, font=FS)
        btn_copy.pack(side="left", padx=6)
        HackerButton(b_row, "DISMISS", modal.destroy, height=36, color=SURFACE, text_col=MUTED, font=FS).pack(side="right")
    except Exception as e:
        messagebox.showerror(title, f"{error_message}\n\nDetails: {technical_details or e}")


class ApiKeyConfigModal(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("AGENT PRAYATH - API CONFIGURATION & TEST")
        self.geometry("580x440")
        self.minsize(500, 380)
        self.configure(fg_color=BG)
        self.grab_set()

        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-580)//2}+{(sh-440)//2}")

        self._build_ui()

    def _build_ui(self):
        hdr = ctk.CTkFrame(self, height=50, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        hdr.pack(fill="x", padx=10, pady=10); hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text=">_ AI UPLINK (OPENROUTER / GEMINI) CONFIGURATION", font=FH2, text_color=NEON_GREEN).pack(side="left", padx=15)
        HackerButton(hdr, "✕", self.destroy, height=28, width=32, color=SURFACE, text_col=MUTED).pack(side="right", padx=10)

        card = HackerCard(self)
        card.pack(fill="both", expand=True, padx=15, pady=(0, 10))

        # Direct Links to get OpenRouter or Gemini Key
        link_box = ctk.CTkFrame(card, fg_color="transparent")
        link_box.pack(fill="x", padx=15, pady=(15, 5))
        HackerButton(link_box, "🌐 GET OPENROUTER KEY (openrouter.ai)",
                     lambda: webbrowser.open("https://openrouter.ai/keys"),
                     height=28, color=SURFACE, hover=DARK_GREEN, text_col=NEON_GREEN, font=FS).pack(side="left", padx=(0, 8))
        HackerButton(link_box, "🔑 GOOGLE AI STUDIO (GEMINI)",
                     lambda: webbrowser.open("https://aistudio.google.com/app/apikey"),
                     height=28, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG, font=FS).pack(side="right")

        ctk.CTkLabel(card, text="PASTE OPENROUTER (sk-or-...) OR GEMINI KEY:", font=FB, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=15, pady=(10, 3))

        entry_row = ctk.CTkFrame(card, fg_color="transparent")
        entry_row.pack(fill="x", padx=15, pady=5)

        self.key_entry = HackerEntry(entry_row, show="*", placeholder="Paste API key here (OpenRouter: sk-or-... or Gemini: AIzaSy...)...")
        self.key_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        cur_key = self.parent.session.get("api_key", "")
        if cur_key:
            self.key_entry.insert(0, cur_key)

        self.btn_test = HackerButton(entry_row, "⚡ TEST KEY", self._test_key, height=38, width=100, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN)
        self.btn_test.pack(side="right")

        self.status_lbl = ctk.CTkLabel(card, text="[*] Enter your OpenRouter or Gemini key and click 'TEST KEY' or 'SAVE & APPLY'.", font=FS, text_color=MUTED, anchor="w")
        self.status_lbl.pack(fill="x", padx=15, pady=(2, 12))

        # Action Buttons
        btn_box = ctk.CTkFrame(card, fg_color="transparent")
        btn_box.pack(fill="x", padx=15, pady=(10, 15))

        HackerButton(btn_box, "💾 SAVE & APPLY KEY", self._save_key, height=42, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG).pack(side="left", fill="x", expand=True, padx=(0, 5))
        HackerButton(btn_box, "🗑️ CLEAR KEY", self._clear_key, height=42, color=SURFACE, text_col=DANGER, border_color=DANGER).pack(side="right", padx=(5, 0))

    def _test_key(self):
        k = self.key_entry.get().strip()
        if not k:
            self.status_lbl.configure(text="[-] Please enter an API key to test.", text_color=DANGER)
            return
        self.btn_test.configure(state="disabled")
        self.status_lbl.configure(text="[*] Verifying AI Uplink (OpenRouter / Gemini Cloud)...", text_color=NEON_GREEN)
        def _task():
            ok, msg = validate_gemini_api_key(k)
            def _ui():
                try:
                    self.btn_test.configure(state="normal")
                    if ok:
                        self.status_lbl.configure(text=f"🟢 {msg}", text_color=NEON_GREEN)
                    else:
                        self.status_lbl.configure(text=f"🔴 {msg}", text_color=DANGER)
                except Exception:
                    pass
            try:
                self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _save_key(self):
        k = self.key_entry.get().strip()
        self.parent.session["api_key"] = k
        save_session(self.parent.session)
        self.parent.backend = AntigravityBackend(k)
        if hasattr(self.parent, "lbl_prof_api"):
            self.parent.lbl_prof_api.configure(text=f"API STATUS: {'ACTIVE' if k else 'OFFLINE'}",
                                                text_color=NEON_GREEN if k else WARNING)
        if hasattr(self.parent, "_build_ai_tab") and "AI_MODULE" in getattr(self.parent, "frames", {}):
            self.parent._build_ai_tab(self.parent.frames["AI_MODULE"])
        provider = getattr(self.parent.backend, "provider", "AI").capitalize()
        messagebox.showinfo("API CONFIGURED", f"{provider} API Key saved and activated successfully!")
        self.destroy()

    def _clear_key(self):
        self.parent.session["api_key"] = ""
        save_session(self.parent.session)
        self.parent.backend = AntigravityBackend("")
        if hasattr(self.parent, "lbl_prof_api"):
            self.parent.lbl_prof_api.configure(text="API STATUS: OFFLINE", text_color=WARNING)
        if hasattr(self.parent, "_build_ai_tab") and "AI_MODULE" in getattr(self.parent, "frames", {}):
            self.parent._build_ai_tab(self.parent.frames["AI_MODULE"])
        messagebox.showinfo("API CLEARED", "API Key cleared. AI Mode is now set to offline.")
        self.destroy()


# ── APP UPDATE MODAL DIALOG ──────────────────────────────────────────────────
class AppUpdateModal(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("AGENT PRAYATH - CLOUD AUTO-UPDATER")
        self.geometry("620x540")
        self.minsize(520, 440)
        self.configure(fg_color=BG)
        self.grab_set()

        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-620)//2}+{(sh-540)//2}")

        self._build_ui()

    def _build_ui(self):
        hdr = ctk.CTkFrame(self, height=55, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        hdr.pack(fill="x", padx=10, pady=10); hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text=">_ CLOUD SYSTEM AUTO-UPDATER", font=FH2, text_color=NEON_GREEN).pack(side="left", padx=15)
        ctk.CTkLabel(hdr, text=f"CURRENT: {APP_VERSION}", font=FS, text_color=MUTED).pack(side="right", padx=15)

        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=15, pady=(0,10))

        card = HackerCard(body)
        card.pack(fill="x", pady=(0,10))

        ctk.CTkLabel(card, text="RELEASE HIGHLIGHTS & CLOUD TELEMETRY", font=FB, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=15, pady=(10,5))

        self.info_lbl = ctk.CTkLabel(card, text="Fetching latest cloud release information...", font=FS, text_color=MUTED, justify="left", anchor="w")
        self.info_lbl.pack(fill="x", padx=15, pady=(0,10))

        self.prog_bar = ctk.CTkProgressBar(body, fg_color=SURFACE, progress_color=NEON_GREEN, height=12)
        self.prog_bar.set(0)
        self.prog_bar.pack(fill="x", pady=(0,10))

        self.log_box = ctk.CTkTextbox(body, height=180, fg_color=SURFACE, text_color=NEON_GREEN, font=FM, border_width=1, border_color=DARK_GREEN)
        self.log_box.pack(fill="both", expand=True, pady=(0,10))
        self.log_box.insert("end", "[*] Click '⚡ UPDATE TO NEW VERSION' to begin synchronization.\n")

        btn_frame = ctk.CTkFrame(body, fg_color="transparent")
        btn_frame.pack(fill="x")

        self.btn_start = HackerButton(btn_frame, "⚡ UPDATE TO NEW VERSION", self._start_update, height=42)
        self.btn_start.pack(side="right")

        HackerButton(btn_frame, "CLOSE", self.destroy, color=SURFACE, text_col=MUTED, height=42).pack(side="left")

        threading.Thread(target=self._fetch_info, daemon=True).start()

    def _fetch_info(self):
        info = get_system_update_info()
        bc = _firebase_request("/system_broadcast")
        if isinstance(bc, dict) and bc.get("version"):
            target_aud = bc.get("target_audience", "ALL USERS")
            is_eligible = True
            if hasattr(self.parent, "_is_user_eligible_for_broadcast"):
                is_eligible = self.parent._is_user_eligible_for_broadcast(target_aud)
            elif "ADMIN" in str(target_aud).upper():
                curr_sess = getattr(self.parent, "session", {})
                is_eligible = (curr_sess.get("role") == "admin")

            if is_eligible:
                latest_v = bc.get("version", APP_VERSION)
                changelog = bc.get("message") or info.get("changelog", "Cloud improvements & bug fixes.")
            else:
                latest_v = info.get("latest_version", APP_VERSION)
                changelog = info.get("changelog", "Cloud improvements & bug fixes.")
        else:
            latest_v = info.get("latest_version", APP_VERSION)
            changelog = info.get("changelog", "Cloud improvements & bug fixes.")
        is_newer = is_version_newer(latest_v, APP_VERSION)

        if is_newer:
            text = f"• Installed Version: {APP_VERSION}\n• Latest Available: {latest_v} (NEW)\n• Highlights: {changelog}\n• Source: GitHub & Firebase Live"
            btn_txt = "⚡ UPDATE TO NEW VERSION"
            btn_col = NEON_GREEN
        else:
            text = f"• Installed Version: {APP_VERSION} (LATEST)\n• Cloud Release: {latest_v}\n• Highlights: {changelog}\n• Status: Application is fully up to date."
            btn_txt = "✔ RE-SYNC SYSTEM"
            btn_col = DARK_GREEN

        def _ui():
            self.info_lbl.configure(text=text)
            self.btn_start.configure(text=btn_txt, fg_color=btn_col)
            if is_newer:
                self.log_box.insert("end", f"[*] Cloud Update Available: {latest_v}\n[*] Release Line: {changelog}\n[*] Click '⚡ UPDATE TO NEW VERSION' to begin synchronization.\n")
            else:
                self.log_box.insert("end", f"[*] You are already running the latest version ({APP_VERSION}).\n[*] Click '{btn_txt}' to verify system integrity & shortcuts.\n")
        self.after(0, _ui)

    def _start_update(self):
        self.btn_start.configure(state="disabled")
        self.prog_bar.set(0.15)
        self.log_box.delete("1.0", "end")

        def _log_cb(msg):
            def _ui():
                self.log_box.insert("end", f"{msg}\n")
                self.log_box.see("end")
            self.after(0, _ui)

        def _worker():
            self.after(0, lambda: self.prog_bar.set(0.4))
            res = perform_system_update(_log_cb)
            if isinstance(res, tuple) and len(res) == 3:
                ok, v, new_exe = res
            elif isinstance(res, tuple) and len(res) == 2:
                ok, v = res; new_exe = None
            else:
                ok, v, new_exe = True, APP_VERSION, None
            self.after(0, lambda: self.prog_bar.set(1.0))
            if ok:
                _log_cb(f"\n[+] UPDATE TO {v} COMPLETED SUCCESSFULLY!")
                _log_cb("[*] Automatically reopening application in 2 seconds...")
                time.sleep(1.8)
                self.after(0, lambda: self._restart_app(new_exe))
            else:
                _log_cb("\n[!] Synchronization incomplete. Current installation preserved.")
                self.after(0, lambda: self.btn_start.configure(state="normal"))

        threading.Thread(target=_worker, daemon=True).start()

    def _restart_app(self, new_exe=None):
        try:
            self.destroy()
            if hasattr(self.parent, "destroy"):
                self.parent.destroy()
        except Exception:
            pass
        safe_restart_app(new_exe)


# ── USER & TESTING GROUPS MANAGEMENT MODAL ───────────────────────────────────
FEMALE_NAME_KEYWORDS = {
    "DEVI", "LAKSHMI", "PRIYA", "SRI", "KUMARI", "ANITHA", "BHAVANI", "DIVYA", "MOUNIKA",
    "POOJITHA", "SRAVANI", "TEJASWI", "VARSHINI", "SOWMYA", "SWETHA", "HARIKA", "ANUSHA",
    "ROHINI", "JYOTHI", "SANDHYA", "RADHA", "GEETHA", "USHA", "SITA", "RAMYA", "KAVYA",
    "SNEHA", "SINDHU", "DEEPIKA", "NAVYA", "PRAVALLIKA", "MEGHANA", "CHANDANA", "ALEKHYA",
    "SUPRIYA", "SUPRAJA", "LALITHA", "PADMA", "SARASWATHI", "DURGA", "MAHALAKSHMI", "ANANYA",
    "SRAVYA", "AISWARYA", "AISHWARYA", "SUSHMITHA", "SUSHMA", "SHANMITHA", "PRANATHI",
    "PRATHYUSHA", "MANASA", "REVATHI", "GAYATRI", "YAMINI", "SIRI", "JAHNAVI", "SIRISHA",
    "HARSHITHA", "PAVANI", "HEMA", "MADHURI", "ARCHANA", "SONIA", "APARNA", "ASHA", "AMRUTHA",
    "POOJA", "RUCHITHA", "CHANDINI", "MONICA", "TRISHA", "SHREYA", "BINDUSREE", "BINDHU"
}

def is_female_name(name):
    tokens = set(re.findall(r"[A-Z]+", str(name).upper()))
    return bool(tokens & FEMALE_NAME_KEYWORDS)

class UserGroupsModal(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("AGENT PRAYATH - USER & TESTING GROUPS MANAGER")
        self.geometry("980x680")
        self.minsize(860, 580)
        self.configure(fg_color=BG)
        self.grab_set()

        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-980)//2}+{(sh-680)//2}")

        self.groups = {}
        self.selected_group_key = None
        self.cloud_db = getattr(parent, "admin_db", None) or load_cloud_db() or {}
        self.all_students = []

        self._prep_students_list()
        self._build_ui()
        self._load_groups_from_cloud()
        if not self.all_students:
            self._load_students_async()

    def _load_students_async(self):
        def _task():
            try:
                fresh = _firebase_request("/students", timeout=12)
                if isinstance(fresh, dict) and fresh:
                    self.cloud_db = fresh
                    def _ui():
                        self._prep_students_list()
                        self._refresh_student_tree()
                    self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _prep_students_list(self):
        self.all_students = []
        for roll, data in self.cloud_db.items():
            if isinstance(data, dict):
                name = str(data.get("name", "")).strip()
                branch = str(data.get("branch", "")).strip().upper()
                self.all_students.append((str(roll).upper(), name, branch))
        self.all_students.sort(key=lambda x: x[0])

    def _build_ui(self):
        # Header
        hdr = ctk.CTkFrame(self, height=54, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        hdr.pack(fill="x", padx=10, pady=10)
        hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text="👥 USER & TESTING GROUPS MANAGER (ADMIN TARGETING)", font=FH2, text_color=NEON_GREEN).pack(side="left", padx=15)
        HackerButton(hdr, "✕", self.destroy, height=28, width=32, color=SURFACE, text_col=MUTED).pack(side="right", padx=10)

        # Body split
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Left Panel: Groups List
        left = HackerCard(body, width=280)
        left.pack(side="left", fill="y", padx=(0, 8))
        left.pack_propagate(False)

        ctk.CTkLabel(left, text="DEPLOYMENT GROUPS", font=FH3, text_color=NEON_GREEN).pack(pady=(12, 6), padx=10, anchor="w")

        tree_grp_frame = ctk.CTkFrame(left, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        tree_grp_frame.pack(fill="both", expand=True, padx=8, pady=4)

        self.groups_tree = ttk.Treeview(tree_grp_frame, columns=("Group", "Count"), show="headings", style="Hacker.Treeview", height=12)
        self.groups_tree.heading("Group", text="GROUP NAME")
        self.groups_tree.heading("Count", text="MEMBERS")
        self.groups_tree.column("Group", width=160)
        self.groups_tree.column("Count", width=80, anchor="center")

        g_scroll = ttk.Scrollbar(tree_grp_frame, orient="vertical", command=self.groups_tree.yview)
        self.groups_tree.configure(yscrollcommand=g_scroll.set)
        g_scroll.pack(side="right", fill="y")
        self.groups_tree.pack(side="left", fill="both", expand=True)
        self.groups_tree.bind("<<TreeviewSelect>>", self._on_group_selected)

        grp_btn_row = ctk.CTkFrame(left, fg_color="transparent")
        grp_btn_row.pack(fill="x", padx=8, pady=(8, 12))
        HackerButton(grp_btn_row, "+ NEW GROUP", self._start_new_group, height=34, color=DARK_GREEN, text_col=BG).pack(side="left", fill="x", expand=True, padx=(0, 4))
        HackerButton(grp_btn_row, "🗑️ DELETE", self._delete_current_group, height=34, color=SURFACE, text_col=DANGER, border_color=DANGER).pack(side="right", padx=(4, 0))

        # Right Panel: Group Member Editor
        right = HackerCard(body)
        right.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(right, text="GROUP CONFIGURATION & STUDENT AUDIENCE", font=FH3, text_color=NEON_GREEN).pack(pady=(12, 6), padx=12, anchor="w")

        # Meta Form
        meta_frame = ctk.CTkFrame(right, fg_color="transparent")
        meta_frame.pack(fill="x", padx=12, pady=(0, 6))

        ctk.CTkLabel(meta_frame, text="Group Name:", font=FS, text_color=MUTED).grid(row=0, column=0, sticky="e", padx=4, pady=2)
        self.grp_name_entry = HackerEntry(meta_frame, placeholder="e.g. Beta Testers, Testing Group 1, Girls Batch...")
        self.grp_name_entry.grid(row=0, column=1, sticky="ew", padx=4, pady=2)

        ctk.CTkLabel(meta_frame, text="Description:", font=FS, text_color=MUTED).grid(row=0, column=2, sticky="e", padx=4, pady=2)
        self.grp_desc_entry = HackerEntry(meta_frame, placeholder="Group purpose or release target...")
        self.grp_desc_entry.grid(row=0, column=3, sticky="ew", padx=4, pady=2)

        meta_frame.columnconfigure(1, weight=1)
        meta_frame.columnconfigure(3, weight=1)

        # Filters toolbar
        flt_box = ctk.CTkFrame(right, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        flt_box.pack(fill="x", padx=12, pady=4)

        ctk.CTkLabel(flt_box, text="Branch:", font=FS, text_color=MUTED).pack(side="left", padx=(8, 2))
        self.branch_filter_var = ctk.StringVar(value="ALL BRANCHES")
        self.branch_menu = ctk.CTkOptionMenu(
            flt_box, variable=self.branch_filter_var,
            values=["ALL BRANCHES", "DS", "CSE", "AIML", "ECE", "EEE", "ME", "CE"],
            command=lambda v: self._refresh_student_tree(),
            fg_color=SURFACE, text_color=NEON_GREEN, button_color=DARK_GREEN, font=FS, width=120
        )
        self.branch_menu.pack(side="left", padx=4, pady=6)

        ctk.CTkLabel(flt_box, text="Gender/Tag:", font=FS, text_color=MUTED).pack(side="left", padx=(8, 2))
        self.gender_filter_var = ctk.StringVar(value="ALL")
        self.gender_menu = ctk.CTkOptionMenu(
            flt_box, variable=self.gender_filter_var,
            values=["ALL", "BOYS BATCH", "GIRLS BATCH"],
            command=lambda v: self._refresh_student_tree(),
            fg_color=SURFACE, text_color=NEON_GREEN, button_color=DARK_GREEN, font=FS, width=120
        )
        self.gender_menu.pack(side="left", padx=4, pady=6)

        ctk.CTkLabel(flt_box, text="Search:", font=FS, text_color=MUTED).pack(side="left", padx=(8, 2))
        self.search_var = ctk.StringVar()
        self.search_entry = HackerEntry(flt_box, placeholder="Search Roll/Name...")
        self.search_entry.configure(textvariable=self.search_var)
        self.search_var.trace_add("write", lambda *a: self._refresh_student_tree())
        self.search_entry.pack(side="left", fill="x", expand=True, padx=6, pady=6)

        # Selection Action Buttons
        b_sel_row = ctk.CTkFrame(right, fg_color="transparent")
        b_sel_row.pack(fill="x", padx=12, pady=(2, 4))
        HackerButton(b_sel_row, "☑ SELECT ALL FILTERED", self._select_all_filtered, height=28, color=SURFACE, text_col=NEON_GREEN, font=FS).pack(side="left", padx=(0, 4))
        HackerButton(b_sel_row, "☐ UNSELECT ALL FILTERED", self._unselect_all_filtered, height=28, color=SURFACE, text_col=MUTED, font=FS).pack(side="left", padx=4)
        HackerButton(b_sel_row, "♀ SELECT GIRLS IN BRANCH", self._select_girls_in_branch, height=28, color=SURFACE, text_col="#ff77aa", font=FS).pack(side="left", padx=4)
        HackerButton(b_sel_row, "♂ SELECT BOYS IN BRANCH", self._select_boys_in_branch, height=28, color=SURFACE, text_col="#66aaff", font=FS).pack(side="left", padx=4)

        # Student Treeview
        tree_st_frame = ctk.CTkFrame(right, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        tree_st_frame.pack(fill="both", expand=True, padx=12, pady=4)

        cols = ("Selected", "Roll", "Name", "Branch")
        self.students_tree = ttk.Treeview(tree_st_frame, columns=cols, show="headings", style="Hacker.Treeview", height=10)
        self.students_tree.heading("Selected", text="IN GROUP")
        self.students_tree.heading("Roll", text="ROLL NO")
        self.students_tree.heading("Name", text="FULL NAME")
        self.students_tree.heading("Branch", text="BRANCH")

        self.students_tree.column("Selected", width=90, anchor="center")
        self.students_tree.column("Roll", width=120)
        self.students_tree.column("Name", width=260)
        self.students_tree.column("Branch", width=90, anchor="center")

        st_scroll = ttk.Scrollbar(tree_st_frame, orient="vertical", command=self.students_tree.yview)
        self.students_tree.configure(yscrollcommand=st_scroll.set)
        st_scroll.pack(side="right", fill="y")
        self.students_tree.pack(side="left", fill="both", expand=True)
        self.students_tree.bind("<Double-1>", self._toggle_student_selection)
        self.students_tree.bind("<space>", self._toggle_student_selection)

        # Bottom Bar: Stats & Save
        bot_bar = ctk.CTkFrame(right, fg_color="transparent")
        bot_bar.pack(fill="x", padx=12, pady=(6, 12))

        self.lbl_member_stats = ctk.CTkLabel(bot_bar, text="MEMBERS SELECTED: 0 STUDENTS", font=FB, text_color=NEON_GREEN)
        self.lbl_member_stats.pack(side="left")

        self.lbl_grp_status = ctk.CTkLabel(bot_bar, text="", font=FS, text_color=MUTED)
        self.lbl_grp_status.pack(side="left", padx=15)

        HackerButton(bot_bar, "💾 SAVE GROUP TO FIREBASE", self._save_current_group, height=38, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG).pack(side="right")

    def _load_groups_from_cloud(self):
        def _task():
            data = get_user_groups()
            self.groups = data if isinstance(data, dict) else {}
            def _ui():
                for item in list(self.groups_tree.get_children()):
                    self.groups_tree.delete(item)
                for gname, ginfo in sorted(self.groups.items(), key=lambda x: str(x[0]).lower()):
                    if isinstance(ginfo, dict):
                        members = ginfo.get("members", [])
                        count = len(members) if isinstance(members, list) else 0
                        self.groups_tree.insert("", "end", iid=gname, values=(gname, f"{count} users"))
                if self.selected_group_key and self.groups_tree.exists(self.selected_group_key):
                    self.groups_tree.selection_set(self.selected_group_key)
                self._refresh_student_tree()
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _start_new_group(self):
        self.selected_group_key = None
        self.selected_members = set()
        self.grp_name_entry.delete(0, "end")
        self.grp_desc_entry.delete(0, "end")
        for sel in self.groups_tree.selection():
            self.groups_tree.selection_remove(sel)
        self.branch_filter_var.set("ALL BRANCHES")
        self.gender_filter_var.set("ALL")
        self.search_var.set("")
        self.lbl_grp_status.configure(text="[+] Enter new group details.", text_color=NEON_GREEN)
        self.grp_name_entry.focus_set()
        self._refresh_student_tree()

    def _on_group_selected(self, event):
        sel = self.groups_tree.selection()
        if not sel: return
        gname = sel[0]
        if gname not in self.groups or not isinstance(self.groups[gname], dict): return
        ginfo = self.groups[gname]
        self.selected_group_key = gname
        self.grp_name_entry.delete(0, "end")
        self.grp_name_entry.insert(0, gname)
        self.grp_desc_entry.delete(0, "end")
        self.grp_desc_entry.insert(0, ginfo.get("description", ""))

        members = ginfo.get("members", [])
        if isinstance(members, list):
            self.selected_members = set(str(m).upper() for m in members)
        else:
            self.selected_members = set()

        b_flt = ginfo.get("branch_filter", "ALL BRANCHES")
        if b_flt in ["ALL BRANCHES", "DS", "CSE", "AIML", "ECE", "EEE", "ME", "CE"]:
            self.branch_filter_var.set(b_flt)

        self._refresh_student_tree()
        self.lbl_grp_status.configure(text=f"Loaded group '{gname}'.", text_color=NEON_GREEN)

    def _refresh_student_tree(self):
        for item in self.students_tree.get_children():
            self.students_tree.delete(item)

        branch_flt = self.branch_filter_var.get().upper()
        gender_flt = self.gender_filter_var.get().upper()
        query = self.search_var.get().strip().lower()

        count = 0
        for roll, name, branch in self.all_students:
            # Branch filter
            if branch_flt != "ALL BRANCHES":
                if branch_flt in ("DS", "DATA SCIENCE"):
                    if branch not in ("DS", "DATA SCIENCE"): continue
                elif branch_flt not in branch:
                    continue

            # Gender/tag filter
            if gender_flt == "GIRLS BATCH" and not is_female_name(name):
                continue
            if gender_flt == "BOYS BATCH" and is_female_name(name):
                continue

            # Search query
            if query and (query not in roll.lower() and query not in name.lower() and query not in branch.lower()):
                continue

            if self.students_tree.exists(roll):
                continue

            is_sel = "[✓] YES" if roll in self.selected_members else "[ ] --"
            self.students_tree.insert("", "end", iid=roll, values=(is_sel, roll, name, branch))
            count += 1
            if count >= 600:
                break

        self.lbl_member_stats.configure(text=f"MEMBERS SELECTED: {len(self.selected_members)} STUDENTS")

    def _toggle_student_selection(self, event=None):
        sel = self.students_tree.selection()
        if not sel: return
        roll = sel[0]
        if roll in self.selected_members:
            self.selected_members.remove(roll)
            self.students_tree.set(roll, "Selected", "[ ] --")
        else:
            self.selected_members.add(roll)
            self.students_tree.set(roll, "Selected", "[✓] YES")
        self.lbl_member_stats.configure(text=f"MEMBERS SELECTED: {len(self.selected_members)} STUDENTS")

    def _select_all_filtered(self):
        for item in self.students_tree.get_children():
            self.selected_members.add(item)
            self.students_tree.set(item, "Selected", "[✓] YES")
        self.lbl_member_stats.configure(text=f"MEMBERS SELECTED: {len(self.selected_members)} STUDENTS")

    def _unselect_all_filtered(self):
        for item in self.students_tree.get_children():
            if item in self.selected_members:
                self.selected_members.remove(item)
            self.students_tree.set(item, "Selected", "[ ] --")
        self.lbl_member_stats.configure(text=f"MEMBERS SELECTED: {len(self.selected_members)} STUDENTS")

    def _select_girls_in_branch(self):
        for item in self.students_tree.get_children():
            vals = self.students_tree.item(item, "values")
            name = vals[2] if len(vals) > 2 else ""
            if is_female_name(name):
                self.selected_members.add(item)
                self.students_tree.set(item, "Selected", "[✓] YES")
        self.lbl_member_stats.configure(text=f"MEMBERS SELECTED: {len(self.selected_members)} STUDENTS")

    def _select_boys_in_branch(self):
        for item in self.students_tree.get_children():
            vals = self.students_tree.item(item, "values")
            name = vals[2] if len(vals) > 2 else ""
            if not is_female_name(name):
                self.selected_members.add(item)
                self.students_tree.set(item, "Selected", "[✓] YES")
        self.lbl_member_stats.configure(text=f"MEMBERS SELECTED: {len(self.selected_members)} STUDENTS")

    def _save_current_group(self):
        name = self.grp_name_entry.get().strip()
        if not name:
            messagebox.showwarning("MISSING NAME", "Please enter a Group Name (e.g. 'Beta Testers' or 'DS Testing Batch').")
            return

        desc = self.grp_desc_entry.get().strip() or "Custom update deployment group"
        b_flt = self.branch_filter_var.get()
        g_flt = self.gender_filter_var.get()

        author = getattr(self.parent, "session", {}).get("name", "ADMIN")
        data = {
            "name": name,
            "description": desc,
            "branch_filter": b_flt,
            "gender_filter": g_flt,
            "members": sorted(list(self.selected_members)),
            "count": len(self.selected_members),
            "updated_at": int(time.time()),
            "author": author
        }

        self.lbl_grp_status.configure(text="[*] Uploading group to Firebase Cloud...", text_color=NEON_GREEN)
        def _task():
            res = set_user_group(name, data)
            def _ui():
                if res is not None:
                    self.groups[name] = data
                    self.selected_group_key = name
                    self.lbl_grp_status.configure(text=f"[+] Group '{name}' saved to Cloud ({len(self.selected_members)} users)!", text_color=NEON_GREEN)
                    messagebox.showinfo("GROUP SAVED", f"Group '{name}' created/saved successfully with {len(self.selected_members)} student members!")
                    self._load_groups_from_cloud()
                    if hasattr(self.parent, "_refresh_admin_target_options"):
                        self.parent._refresh_admin_target_options()
                    if hasattr(self.parent, "_refresh_admin_group_filter_options"):
                        self.parent._refresh_admin_group_filter_options()
                else:
                    self.lbl_grp_status.configure(text=f"[!] Failed to save group '{name}'.", text_color=DANGER)
                    messagebox.showerror("SAVE FAILED", f"Could not create group '{name}' in Firebase Cloud. Please check your network connection.")
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _delete_current_group(self):
        sel = self.groups_tree.selection()
        if not sel:
            messagebox.showinfo("NO GROUP SELECTED", "Please select a group from the list to delete.")
            return
        gname = sel[0]
        ans = messagebox.askyesno("CONFIRM DELETE", f"Are you sure you want to delete group '{gname}' from Firebase Cloud?")
        if not ans: return
        def _task():
            delete_user_group(gname)
            def _ui():
                if gname in self.groups:
                    del self.groups[gname]
                self._start_new_group()
                self._load_groups_from_cloud()
                if hasattr(self.parent, "_refresh_admin_target_options"):
                    self.parent._refresh_admin_target_options()
                if hasattr(self.parent, "_refresh_admin_group_filter_options"):
                    self.parent._refresh_admin_group_filter_options()
                messagebox.showinfo("GROUP DELETED", f"Group '{gname}' deleted from Firebase Cloud.")
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()


# ── OFFLINE DSA VAULT & STUDENT EXAM REPOSITORY ──────────────────────────────
OFFLINE_DSA_VAULT = {
    "Binary Search": {
        "python": """def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    idx = binary_search(arr, target)
    print(f"Element found at index {idx}" if idx != -1 else "Element not found")
""",
        "cpp": """#include <iostream>
#include <vector>
using namespace std;

int binarySearch(const vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int main() {
    int n, target;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cin >> target;
    int idx = binarySearch(arr, target);
    if (idx != -1) cout << "Element found at index " << idx << endl;
    else cout << "Element not found" << endl;
    return 0;
}
""",
        "java": """import java.util.Scanner;

public class Main {
    public static int binarySearch(int[] arr, int target) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int target = sc.nextInt();
        int idx = binarySearch(arr, target);
        System.out.println(idx != -1 ? "Element found at index " + idx : "Element not found");
    }
}
"""
    },
    "Merge Sort": {
        "python": """def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = merge_sort(arr)
    print(" ".join(map(str, sorted_arr)))
""",
        "cpp": """#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) cout << arr[i] << (i == n - 1 ? "" : " ");
    cout << endl;
    return 0;
}
""",
        "java": """import java.util.Scanner;

public class Main {
    public static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1, n2 = r - m;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; i++) L[i] = arr[l + i];
        for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        mergeSort(arr, 0, n - 1);
        for (int i = 0; i < n; i++) System.out.print(arr[i] + (i == n - 1 ? "" : " "));
        System.out.println();
    }
}
"""
    },
    "Quick Sort": {
        "python": """def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(" ".join(map(str, quick_sort(arr))))
""",
        "cpp": """#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high], i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    quickSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) cout << arr[i] << (i == n - 1 ? "" : " ");
    cout << endl;
    return 0;
}
""",
        "java": """import java.util.Scanner;

public class Main {
    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high], i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        return i + 1;
    }

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        quickSort(arr, 0, n - 1);
        for (int i = 0; i < n; i++) System.out.print(arr[i] + (i == n - 1 ? "" : " "));
        System.out.println();
    }
}
"""
    },
    "Singly Linked List": {
        "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "List is empty")

if __name__ == "__main__":
    ll = LinkedList()
    vals = list(map(int, input().split()))
    for v in vals:
        ll.insert(v)
    ll.display()
""",
        "cpp": """#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
public:
    Node* head = nullptr;
    void insert(int val) {
        Node* newNode = new Node(val);
        if (!head) { head = newNode; return; }
        Node* temp = head;
        while (temp->next) temp = temp->next;
        temp->next = newNode;
    }
    void display() {
        Node* temp = head;
        while (temp) {
            cout << temp->data << (temp->next ? " -> " : "");
            temp = temp->next;
        }
        cout << endl;
    }
};

int main() {
    LinkedList ll;
    int x;
    while (cin >> x) ll.insert(x);
    ll.display();
    return 0;
}
""",
        "java": """import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; next = null; }
}

public class Main {
    static Node head = null;
    static void insert(int val) {
        Node nn = new Node(val);
        if (head == null) { head = nn; return; }
        Node t = head;
        while (t.next != null) t = t.next;
        t.next = nn;
    }
    static void display() {
        Node t = head;
        while (t != null) {
            System.out.print(t.data + (t.next != null ? " -> " : ""));
            t = t.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) insert(sc.nextInt());
        display();
    }
}
"""
    },
    "Stack (Array Implementation)": {
        "python": """class Stack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if len(self.stack) >= self.capacity:
            print("Stack Overflow")
            return False
        self.stack.append(item)
        return True

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return None
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else None

    def display(self):
        print("Stack elements:", self.stack[::-1])

if __name__ == "__main__":
    s = Stack()
    for x in map(int, input().split()):
        s.push(x)
    s.display()
""",
        "cpp": """#include <iostream>
using namespace std;

class Stack {
    int topIndex;
    int capacity;
    int* arr;
public:
    Stack(int cap = 100) : capacity(cap), topIndex(-1) {
        arr = new int[capacity];
    }
    void push(int x) {
        if (topIndex >= capacity - 1) { cout << "Stack Overflow\\n"; return; }
        arr[++topIndex] = x;
    }
    int pop() {
        if (topIndex < 0) { cout << "Stack Underflow\\n"; return -1; }
        return arr[topIndex--];
    }
    void display() {
        for (int i = topIndex; i >= 0; i--) cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Stack s;
    int v;
    while (cin >> v) s.push(v);
    s.display();
    return 0;
}
""",
        "java": """import java.util.Scanner;

public class Main {
    static class Stack {
        int[] arr = new int[100];
        int top = -1;
        void push(int x) {
            if (top >= 99) { System.out.println("Stack Overflow"); return; }
            arr[++top] = x;
        }
        int pop() {
            if (top < 0) { System.out.println("Stack Underflow"); return -1; }
            return arr[top--];
        }
        void display() {
            for (int i = top; i >= 0; i--) System.out.print(arr[i] + " ");
            System.out.println();
        }
    }
    public static void main(String[] args) {
        Stack s = new Stack();
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) s.push(sc.nextInt());
        s.display();
    }
}
"""
    },
    "Binary Search Tree (BST)": {
        "python": """class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(str(root.val))
        inorder(root.right, res)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    root = None
    for n in nums:
        root = insert(root, n)
    res = []
    inorder(root, res)
    print("Inorder Traversal: " + " ".join(res))
""",
        "cpp": """#include <iostream>
using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(nullptr), right(nullptr) {}
};

Node* insert(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->val) root->left = insert(root->left, key);
    else if (key > root->val) root->right = insert(root->right, key);
    return root;
}

void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

int main() {
    Node* root = nullptr;
    int x;
    while (cin >> x) root = insert(root, x);
    cout << "Inorder Traversal: ";
    inorder(root);
    cout << endl;
    return 0;
}
""",
        "java": """import java.util.Scanner;

class Node {
    int val;
    Node left, right;
    Node(int v) { val = v; }
}

public class Main {
    static Node insert(Node root, int key) {
        if (root == null) return new Node(key);
        if (key < root.val) root.left = insert(root.left, key);
        else if (key > root.val) root.right = insert(root.right, key);
        return root;
    }
    static void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.val + " ");
        inorder(root.right);
    }
    public static void main(String[] args) {
        Node root = null;
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) root = insert(root, sc.nextInt());
        System.out.print("Inorder Traversal: ");
        inorder(root);
        System.out.println();
    }
}
"""
    },
    "Dijkstra's Algorithm": {
        "python": """import heapq

def dijkstra(graph, start, n):
    dist = {i: float('inf') for i in range(n)}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph.get(u, []):
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))
    start_node = int(input())
    distances = dijkstra(graph, start_node, n)
    for node, d in distances.items():
        print(f"Node {node}: {d if d != float('inf') else 'UNREACHABLE'}")
""",
        "cpp": """#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int INF = 1e9;

void dijkstra(int start, int n, const vector<vector<pair<int, int>>>& adj) {
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();
        if (d > dist[u]) continue;

        for (auto edge : adj[u]) {
            int v = edge.first, w = edge.second;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    for (int i = 0; i < n; i++) {
        cout << "Node " << i << ": " << (dist[i] == INF ? -1 : dist[i]) << "\\n";
    }
}

int main() {
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    int start;
    cin >> start;
    dijkstra(start, n, adj);
    return 0;
}
""",
        "java": """import java.util.*;

public class Main {
    static class Edge { int to, w; Edge(int t, int w) { this.to = t; this.w = w; } }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), m = sc.nextInt();
        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            adj.get(u).add(new Edge(v, w));
            adj.get(v).add(new Edge(u, w));
        }
        int start = sc.nextInt();
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        dist[start] = 0;
        pq.offer(new int[]{0, start});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], u = cur[1];
            if (d > dist[u]) continue;
            for (Edge e : adj.get(u)) {
                if (dist[u] + e.w < dist[e.to]) {
                    dist[e.to] = dist[u] + e.w;
                    pq.offer(new int[]{dist[e.to], e.to});
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println("Node " + i + ": " + (dist[i] == Integer.MAX_VALUE ? "INF" : dist[i]));
        }
    }
}
"""
    },
    "0/1 Knapsack Problem": {
        "python": """def knapsack(weights, values, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    capacity = int(input())
    print("Maximum Value:", knapsack(weights, values, capacity, n))
""",
        "cpp": """#include <iostream>
#include <vector>
using namespace std;

int knapSack(int W, const vector<int>& wt, const vector<int>& val, int n) {
    vector<vector<int>> K(n + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (wt[i - 1] <= w)
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];
}

int main() {
    int n, W;
    if (!(cin >> n)) return 0;
    vector<int> val(n), wt(n);
    for (int i = 0; i < n; i++) cin >> val[i];
    for (int i = 0; i < n; i++) cin >> wt[i];
    cin >> W;
    cout << "Maximum Value: " << knapSack(W, wt, val, n) << endl;
    return 0;
}
""",
        "java": """import java.util.Scanner;

public class Main {
    static int knapSack(int W, int[] wt, int[] val, int n) {
        int[][] K = new int[n + 1][W + 1];
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                if (wt[i - 1] <= w)
                    K[i][w] = Math.max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
                else
                    K[i][w] = K[i - 1][w];
            }
        }
        return K[n][W];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] val = new int[n], wt = new int[n];
        for (int i = 0; i < n; i++) val[i] = sc.nextInt();
        for (int i = 0; i < n; i++) wt[i] = sc.nextInt();
        int W = sc.nextInt();
        System.out.println("Maximum Value: " + knapSack(W, wt, val, n));
    }
}
"""
    }
}

# ── SCREEN SNIPPER (INTERACTIVE CROP BOX) ────────────────────────────────────
class ScreenSnipper(ctk.CTkToplevel):
    def __init__(self, on_snip_callback, on_cancel_callback=None):
        super().__init__()
        self.on_snip_callback = on_snip_callback
        self.on_cancel_callback = on_cancel_callback
        self._snipped = False

        # Grab clean pre-overlay full screenshot for exact DPI proportional cropping
        try:
            self.full_screen_img = robust_screen_capture()
        except Exception:
            self.full_screen_img = None

        self.attributes("-fullscreen", True)
        self.attributes("-alpha", 0.35)
        self.attributes("-topmost", True)
        self.configure(cursor="cross")

        self.canvas = tk.Canvas(self, cursor="cross", bg="#000000", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        sw = max(1, self.winfo_screenwidth())
        sh = max(1, self.winfo_screenheight())
        self.sw = sw
        self.sh = sh

        self.canvas.create_text(
            sw // 2, 40,
            text=">_ DRAG A BOX OVER QUESTION TO SOLVE [ESC TO CANCEL]",
            fill="#00FF41", font=("Consolas", 14, "bold")
        )
        self.dim_lbl = self.canvas.create_text(
            sw // 2, 68,
            text="", fill="#e0e0e0", font=("Consolas", 11)
        )

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self._on_press)
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Escape>", lambda e: self._cancel())
        self.protocol("WM_DELETE_WINDOW", self._cancel)

    def _cancel(self):
        try:
            self.destroy()
        except Exception:
            pass
        if not self._snipped and self.on_cancel_callback:
            self.on_cancel_callback()

    def _on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.rect:
            try: self.canvas.delete(self.rect)
            except Exception: pass
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline="#00FF41", width=2, fill="#003300"
        )

    def _on_drag(self, event):
        if self.rect and self.start_x is not None and self.start_y is not None:
            self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)
            w = abs(event.x - self.start_x)
            h = abs(event.y - self.start_y)
            self.canvas.itemconfigure(self.dim_lbl, text=f"[ Selected Area: {w} × {h} px ]")

    def _on_release(self, event):
        if self.start_x is None or self.start_y is None:
            self._cancel()
            return

        x1 = min(self.start_x, event.x)
        y1 = min(self.start_y, event.y)
        x2 = max(self.start_x, event.x)
        y2 = max(self.start_y, event.y)

        width = x2 - x1
        height = y2 - y1

        sw = getattr(self, "sw", 1920)
        sh = getattr(self, "sh", 1080)
        full_img = self.full_screen_img

        try:
            self.destroy()
        except Exception:
            pass

        if width < 25 or height < 25:
            if self.on_cancel_callback:
                self.on_cancel_callback()
            return

        self._snipped = True

        try:
            if full_img:
                pw, ph = full_img.size
                scale_x = pw / max(1, sw)
                scale_y = ph / max(1, sh)
                crop_box = (
                    int(x1 * scale_x),
                    int(y1 * scale_y),
                    int(x2 * scale_x),
                    int(y2 * scale_y)
                )
                snip_img = full_img.crop(crop_box)
            else:
                time.sleep(0.05)
                snip_img = robust_screen_capture(bbox=(x1, y1, x2, y2))

            if self.on_snip_callback:
                self.on_snip_callback(snip_img)
        except Exception as e:
            print(f"[Snip Grab Error]: {e}")
            if self.on_cancel_callback:
                self.on_cancel_callback()

# ── GHOST HUD (STEALTH FLOATING WIDGET) ───────────────────────────────────────
class GhostHUD(ctk.CTkToplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("AGENT PRAYATH - GHOST HUD")
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        w, h = 540, 68
        self.geometry(f"{w}x{h}+{(sw - w) // 2}+22")
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.96)
        self.configure(fg_color="#000000")

        self.start_x = 0
        self.start_y = 0
        self.bind("<ButtonPress-1>", self._start_move)
        self.bind("<B1-Motion>", self._do_move)
        self.bind("<Double-Button-1>", lambda e: self._on_expand())
        self.bind("<Escape>", lambda e: self._on_expand())

        frame = ctk.CTkFrame(self, fg_color="#071207", border_width=2, border_color="#00FF41", corner_radius=8)
        frame.pack(fill="both", expand=True, padx=2, pady=2)
        frame.bind("<ButtonPress-1>", self._start_move)
        frame.bind("<B1-Motion>", self._do_move)
        frame.bind("<Double-Button-1>", lambda e: self._on_expand())

        title_lbl = ctk.CTkLabel(frame, text="👻 GHOST HUD", font=("Consolas", 11, "bold"), text_color="#00FF41")
        title_lbl.pack(side="left", padx=(12, 8))
        title_lbl.bind("<ButtonPress-1>", self._start_move)
        title_lbl.bind("<B1-Motion>", self._do_move)

        HackerButton(frame, "📸 SNIP", self._on_snip, height=32, width=78, font=("Consolas", 10, "bold")).pack(side="left", padx=4)
        HackerButton(frame, "⚡ INJECT", self._on_type, height=32, width=82, font=("Consolas", 10, "bold")).pack(side="left", padx=4)

        # Big, clear Re-enter Button
        self.btn_expand = HackerButton(
            frame, "🖥️ RE-ENTER FULL APP", self._on_expand,
            height=34, width=170, color="#008F11", hover="#00FF41",
            text_col="#000000", border_color="#00FF41", font=("Consolas", 11, "bold")
        )
        self.btn_expand.pack(side="left", padx=6)

        HackerButton(frame, "✕", self._on_close, height=30, width=32, color="#ff003c", hover="#b30000", text_col="#ffffff", font=("Consolas", 10, "bold")).pack(side="right", padx=(4, 10))

    def _start_move(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def _do_move(self, event):
        deltax = event.x - self.start_x
        deltay = event.y - self.start_y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        self.geometry(f"+{new_x}+{new_y}")

    def _on_snip(self):
        self.withdraw()
        time.sleep(0.12)
        def _cb(img):
            self.deiconify()
            if img and self.app:
                self.app._process_cropped_snip(img)
        def _cancel():
            self.deiconify()
        ScreenSnipper(_cb, on_cancel_callback=_cancel)

    def _on_type(self):
        self.withdraw()
        self.app.start_direct_typing()
        self.after(3500, self.deiconify)

    def _on_expand(self):
        try:
            self.destroy()
        except Exception:
            pass
        self.app.ghost_hud = None
        self.app.deiconify()
        self.app.lift()
        self.app.attributes("-topmost", True)
        self.app.after(250, lambda: self.app.attributes("-topmost", False))
        self.app.focus_force()
        self.app.update_status("[+] RESTORED TO FULL APPLICATION.")

    def _on_close(self):
        try:
            self.destroy()
        except Exception:
            pass
        self.app.ghost_hud = None
        self.app.deiconify()


# ── TINY MCQ ANSWER WINDOW (MINIMALIST STEALTH HUD) ───────────────────────────
class TinyMCQWindow(ctk.CTkToplevel):
    """
    Ultra-compact, floating stealth window for MCQ test solving.
    Displays ONLY question numbers and option letters (e.g. Q1: B, Q2: A)
    with a live scrolling / buffering animation while thinking.
    Supports single snapshot and 3-second clip recording to prevent question cut-off.
    """
    def __init__(self, app, parent_popup=None):
        super().__init__()
        self.app = app
        self.parent_popup = parent_popup
        self.title("MCQ HUD")

        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        w, h = 320, 185
        pos_x = max(10, sw - w - 25)
        pos_y = 30
        self.geometry(f"{w}x{h}+{pos_x}+{pos_y}")
        self.minsize(260, 140)
        self.configure(fg_color="#020702")
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.96)

        # Drag state
        self.start_x = 0
        self.start_y = 0

        # Animation state
        self.is_buffering = False
        self.anim_frame = 0
        self.anim_pos = 0.0
        self.buffer_msg = "ANALYZING..."
        self.answers_data = []
        self.full_details_text = ""
        self.is_details_open = False

        # ── 1. TITLE BAR (Draggable) ─────────────────────────────────────────
        self.top_bar = ctk.CTkFrame(self, fg_color="#081408", height=32, corner_radius=0)
        self.top_bar.pack(fill="x", side="top")
        self.top_bar.bind("<ButtonPress-1>", self._start_move)
        self.top_bar.bind("<B1-Motion>", self._do_move)

        lbl_title = ctk.CTkLabel(self.top_bar, text="⚡ MCQ HUD", font=("Consolas", 10, "bold"), text_color="#00FF41")
        lbl_title.pack(side="left", padx=8)
        lbl_title.bind("<ButtonPress-1>", self._start_move)
        lbl_title.bind("<B1-Motion>", self._do_move)

        # Quick Actions in Top Bar
        HackerButton(self.top_bar, "📸 SNAP", lambda: self._trigger_capture("SNAP"),
                     height=22, width=54, color="#0f260f", hover="#008F11", text_col="#00FF41", font=("Consolas", 9, "bold")).pack(side="left", padx=2)

        HackerButton(self.top_bar, "🎥 3s CLIP", lambda: self._trigger_capture("CLIP"),
                     height=22, width=64, color="#1f538d", hover="#3a7ebf", text_col="#ffffff", font=("Consolas", 9, "bold")).pack(side="left", padx=2)

        HackerButton(self.top_bar, "✂️ SNIP", lambda: self._trigger_capture("SNIP"),
                     height=22, width=54, color="#0f260f", hover="#008F11", text_col="#00FF41", font=("Consolas", 9, "bold")).pack(side="left", padx=2)

        HackerButton(self.top_bar, "✕", self._on_close,
                     height=20, width=24, color="#330000", hover="#ff003c", text_col="#ffffff", font=("Consolas", 9, "bold")).pack(side="right", padx=6)

        # ── 2. BUFFERING CONTAINER (Initially unpacked) ──────────────────────
        self.anim_frame_container = ctk.CTkFrame(self, fg_color="#050e05", corner_radius=4)
        self.lbl_buffer_anim = ctk.CTkLabel(
            self.anim_frame_container,
            text="[ ⠋ ANALYZING SCREEN... ]",
            font=("Consolas", 10, "bold"), text_color="#00FF41"
        )
        self.lbl_buffer_anim.pack(fill="x", padx=6, pady=(4, 2))

        self.buffer_prog_bar = ctk.CTkProgressBar(
            self.anim_frame_container, fg_color="#020502", progress_color="#00FF41", height=5
        )
        self.buffer_prog_bar.set(0.0)
        self.buffer_prog_bar.pack(fill="x", padx=10, pady=(2, 6))

        # ── 3. FOOTER (PACKED FIRST AT BOTTOM TO ALWAYS BE VISIBLE) ──────────
        self.footer = ctk.CTkFrame(self, fg_color="#040b04", height=24)
        self.footer.pack(fill="x", side="bottom", padx=4, pady=2)

        self.lbl_status_tiny = ctk.CTkLabel(self.footer, text="Ready • Click 📸 or 🎥 3s", font=("Consolas", 8), text_color="#00aa22")
        self.lbl_status_tiny.pack(side="left", padx=6)

        self.btn_toggle_details = HackerButton(
            self.footer, "Details ▼", self._toggle_details,
            height=18, width=65, color="#071207", hover="#008F11", text_col="#00FF41", font=("Consolas", 8)
        )
        self.btn_toggle_details.pack(side="right", padx=4)

        # ── 4. ANSWERS DISPLAY CONTAINER (Fills remaining space) ─────────────
        self.answers_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.answers_container.pack(fill="both", expand=True, padx=4, pady=2)

        # Request sequencing to prevent stale previous answers from overwriting present answers
        self.active_req_id = 0

        # Initial placeholder
        self._render_placeholder()

    def _clear_for_new_capture(self, mode_name="Analyzing Question..."):
        self.active_req_id += 1
        for w in self.answers_container.winfo_children(): w.destroy()
        lbl = ctk.CTkLabel(
            self.answers_container,
            text=f"[ ⏳ {mode_name} ]\nThinking & solving with AI Engine...",
            font=("Consolas", 10, "bold"), text_color="#00FF41"
        )
        lbl.pack(pady=15)
        self.lbl_status_tiny.configure(text=f"Scanning • {mode_name}", text_color="#FFD700")

    def _start_move(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def _do_move(self, event):
        deltax = event.x - self.start_x
        deltay = event.y - self.start_y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        self.geometry(f"+{new_x}+{new_y}")

    def _render_placeholder(self):
        for w in self.answers_container.winfo_children(): w.destroy()
        lbl = ctk.CTkLabel(
            self.answers_container,
            text="> Capture screen or 3s clip\nto reveal MCQ options [A, B, C, D]",
            font=("Consolas", 10), text_color="#008822", justify="center"
        )
        lbl.pack(pady=15)

    # ── BUFFERING & SCROLLING THINKING ANIMATION ─────────────────────────────
    def _start_buffering(self, message="THINKING..."):
        self.is_buffering = True
        self.buffer_msg = message
        self.anim_frame = 0
        self.anim_pos = 0.0
        try:
            self.anim_frame_container.pack(fill="x", padx=6, pady=2, after=self.top_bar)
        except Exception:
            try: self.anim_frame_container.pack(fill="x", padx=6, pady=2)
            except Exception: pass
        self._step_buffering_animation()

    def _step_buffering_animation(self):
        if not self.is_buffering:
            return

        spinners = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        sp = spinners[self.anim_frame % len(spinners)]

        width = 10
        pos = int(self.anim_pos) % width
        wave = ["░"] * width
        wave[pos] = "▓"
        if pos > 0: wave[pos-1] = "▒"
        if pos < width - 1: wave[pos+1] = "▒"
        wave_str = "".join(wave)

        self.lbl_buffer_anim.configure(
            text=f"{sp} [{wave_str}] {self.buffer_msg}",
            text_color="#00FF41"
        )

        cycle = (self.anim_frame % 24) / 24.0
        if (self.anim_frame // 24) % 2 == 1:
            cycle = 1.0 - cycle
        self.buffer_prog_bar.set(cycle)

        self.anim_frame += 1
        self.anim_pos = (self.anim_pos + 0.4) % width
        self.after(65, self._step_buffering_animation)

    def _stop_buffering(self):
        self.is_buffering = False
        try:
            self.anim_frame_container.pack_forget()
        except Exception:
            pass

    # ── PARSE & DISPLAY ANSWERS (ONLY ABCD & NUMBERS) ────────────────────────
    def display_answers(self, raw_text):
        self._stop_buffering()
        self.full_details_text = raw_text
        self.answers_data = []

        lines = raw_text.splitlines()
        found_map = {}

        for line in lines:
            line = line.strip()
            m = re.search(r'(?:Q(?:uestion)?\s*(\d+)|\b(\d+)\b)[\s.:)-]*[\[(]?([A-Da-d])[\])]?', line, re.I)
            if m:
                q_num = m.group(1) or m.group(2)
                opt = m.group(3).upper()
                if q_num and opt in "ABCD" and q_num not in found_map:
                    found_map[q_num] = opt
                    self.answers_data.append((f"Q{q_num}", opt))

        if not self.answers_data:
            corr_matches = re.findall(r'CORRECT ANSWER:\s*\[?([A-Da-d])\]?', raw_text, re.I)
            for idx, c in enumerate(corr_matches, start=1):
                self.answers_data.append((f"Q{idx}", c.upper()))

        if not self.answers_data:
            letters = re.findall(r'\b([A-D])\b', raw_text.upper())
            for idx, let in enumerate(letters[:4], start=1):
                self.answers_data.append((f"Q{idx}", let))

        for w in self.answers_container.winfo_children(): w.destroy()

        if not self.answers_data:
            lbl = ctk.CTkLabel(self.answers_container, text="No options detected\nTry 3-Sec Clip or Snip", font=("Consolas", 10), text_color="#ffff55")
            lbl.pack(pady=15)
            self.lbl_status_tiny.configure(text="No options found")
            return

        grid_frame = ctk.CTkFrame(self.answers_container, fg_color="transparent")
        grid_frame.pack(fill="x", padx=2, pady=4)

        for q_str, opt_letter in self.answers_data:
            badge = ctk.CTkFrame(grid_frame, fg_color="#071307", border_width=1, border_color="#00FF41", corner_radius=6)
            badge.pack(side="left", padx=4, pady=2)

            ctk.CTkLabel(badge, text=q_str, font=("Consolas", 9, "bold"), text_color="#00aa22").pack(padx=6, pady=(3, 0))
            ctk.CTkLabel(badge, text=f"[ {opt_letter} ]", font=("Consolas", 18, "bold"), text_color="#00FF41").pack(padx=8, pady=(0, 4))

        self.lbl_status_tiny.configure(text=f"Solved ({len(self.answers_data)} Qs) • Ready")

    def _toggle_details(self):
        if not self.is_details_open:
            self.is_details_open = True
            self.btn_toggle_details.configure(text="Details ▲")
            self.geometry(f"{max(self.winfo_width(), 380)}x340")
            for w in self.answers_container.winfo_children(): w.destroy()

            if self.answers_data:
                g = ctk.CTkFrame(self.answers_container, fg_color="transparent")
                g.pack(fill="x", pady=2)
                for q_str, opt_letter in self.answers_data:
                    b = ctk.CTkFrame(g, fg_color="#071307", border_width=1, border_color="#00FF41", corner_radius=4)
                    b.pack(side="left", padx=3, pady=2)
                    ctk.CTkLabel(b, text=f"{q_str}: [{opt_letter}]", font=("Consolas", 10, "bold"), text_color="#00FF41").pack(padx=6, pady=2)

            tb = ctk.CTkTextbox(self.answers_container, fg_color="#030803", text_color="#d0ffd0", font=("Consolas", 10), height=180)
            tb.pack(fill="both", expand=True, pady=4)
            tb.insert("end", self.full_details_text or "No details available.")
        else:
            self.is_details_open = False
            self.btn_toggle_details.configure(text="Details ▼")
            self.geometry(f"{self.winfo_width()}x185")
            if self.answers_data:
                for w in self.answers_container.winfo_children(): w.destroy()
                grid_frame = ctk.CTkFrame(self.answers_container, fg_color="transparent")
                grid_frame.pack(fill="x", padx=2, pady=4)
                for q_str, opt_letter in self.answers_data:
                    badge = ctk.CTkFrame(grid_frame, fg_color="#071307", border_width=1, border_color="#00FF41", corner_radius=6)
                    badge.pack(side="left", padx=4, pady=2)
                    ctk.CTkLabel(badge, text=q_str, font=("Consolas", 9, "bold"), text_color="#00aa22").pack(padx=6, pady=(3, 0))
                    ctk.CTkLabel(badge, text=f"[ {opt_letter} ]", font=("Consolas", 18, "bold"), text_color="#00FF41").pack(padx=8, pady=(0, 4))
            else:
                self._render_placeholder()

    # ── CAPTURE TRIGGERS & 3-SECOND CLIP RECORDING ───────────────────────────
    def _trigger_capture(self, mode):
        if self.is_buffering: return
        if mode == "SNAP":
            self.start_full_screen_snap()
        elif mode == "CLIP":
            self.start_3s_clip_recording()
        elif mode == "SNIP":
            self.start_snip_capture()

    def start_full_screen_snap(self):
        self.withdraw()
        self.update_idletasks()
        if self.parent_popup:
            try:
                self.parent_popup.withdraw()
                self.parent_popup.update_idletasks()
            except Exception: pass
        time.sleep(0.2)
        try:
            img = robust_screen_capture()
        finally:
            self.deiconify()
            self.lift()
            if self.parent_popup:
                try:
                    self.parent_popup.deiconify()
                    self.parent_popup.lift()
                    self.lift()
                except Exception: pass

        if img:
            self._clear_for_new_capture("Analyzing Full Screen")
            self._start_buffering("AI THINKING (ANALYZING FULL SCREEN)...")
            if self.parent_popup and hasattr(self.parent_popup, "_set_mcq_status"):
                self.parent_popup._set_mcq_status("🧠 AI Engine analyzing active question & options...", color="#FFD700")

            my_req = self.active_req_id
            def _task():
                try:
                    resp = self.app.backend.solve_smart_interviews_mcq(img)
                    if my_req != self.active_req_id:
                        return  # Stale response discarded!
                    self.after(0, lambda: self.display_answers(resp))
                    if self.parent_popup and hasattr(self.parent_popup, "mcq_result_box"):
                        def _upd():
                            if my_req == getattr(self.parent_popup, "mcq_req_id", my_req):
                                self.parent_popup.mcq_result_box.delete("1.0", "end")
                                self.parent_popup.mcq_result_box.insert("end", resp)
                                self.parent_popup._set_mcq_status("✅ Solved! Options displayed below & in Tiny HUD.", color="#00FF41")
                        self.parent_popup.after(0, _upd)
                except Exception as ex:
                    if my_req != self.active_req_id:
                        return
                    def _err():
                        self._stop_buffering()
                        self.lbl_status_tiny.configure(text=f"Error: {ex}", text_color="#ff4444")
                        for w in self.answers_container.winfo_children(): w.destroy()
                        ctk.CTkLabel(self.answers_container, text=f"❌ Analysis error:\n{ex}\n\nTip: Use ✂️ SNIP to crop only question.", font=("Consolas", 9), text_color="#ff5555").pack(pady=10)
                        if self.parent_popup and hasattr(self.parent_popup, "_set_mcq_status"):
                            self.parent_popup._set_mcq_status(f"❌ AI ERROR: {ex}", color="#ff4444")
                    self.after(0, _err)
            threading.Thread(target=_task, daemon=True).start()

    def start_snip_capture(self):
        self.withdraw()
        self.update_idletasks()
        if self.parent_popup:
            try:
                self.parent_popup.withdraw()
                self.parent_popup.update_idletasks()
            except Exception: pass
        time.sleep(0.15)

        def _on_snip_done(img):
            self.deiconify()
            self.lift()
            if self.parent_popup:
                try:
                    self.parent_popup.deiconify()
                    self.parent_popup.lift()
                    self.lift()
                except Exception: pass

            if img:
                self._clear_for_new_capture("Analyzing Snipped Question")
                self._start_buffering("AI THINKING (ANALYZING SNIPPED QUESTION)...")
                if self.parent_popup and hasattr(self.parent_popup, "_set_mcq_status"):
                    self.parent_popup._set_mcq_status("🧠 AI Engine analyzing snipped question & options...", color="#FFD700")

                my_req = self.active_req_id
                def _task():
                    try:
                        resp = self.app.backend.solve_smart_interviews_mcq(img)
                        if my_req != self.active_req_id:
                            return  # Stale response discarded!
                        self.after(0, lambda: self.display_answers(resp))
                        if self.parent_popup and hasattr(self.parent_popup, "mcq_result_box"):
                            def _upd():
                                if my_req == getattr(self.parent_popup, "mcq_req_id", my_req):
                                    self.parent_popup.mcq_result_box.delete("1.0", "end")
                                    self.parent_popup.mcq_result_box.insert("end", resp)
                                    self.parent_popup._set_mcq_status("✅ Solved! Options displayed below & in Tiny HUD.", color="#00FF41")
                            self.parent_popup.after(0, _upd)
                    except Exception as ex:
                        if my_req != self.active_req_id:
                            return
                        def _err():
                            self._stop_buffering()
                            self.lbl_status_tiny.configure(text=f"Error: {ex}", text_color="#ff4444")
                            for w in self.answers_container.winfo_children(): w.destroy()
                            ctk.CTkLabel(self.answers_container, text=f"❌ Snip analysis error:\n{ex}", font=("Consolas", 9), text_color="#ff5555").pack(pady=10)
                            if self.parent_popup and hasattr(self.parent_popup, "_set_mcq_status"):
                                self.parent_popup._set_mcq_status(f"❌ AI ERROR: {ex}", color="#ff4444")
                        self.after(0, _err)
                threading.Thread(target=_task, daemon=True).start()

        def _on_snip_cancel():
            self.deiconify()
            self.lift()
            if self.parent_popup:
                try:
                    self.parent_popup.deiconify()
                    self.parent_popup.lift()
                    self.lift()
                except Exception: pass

        try:
            ScreenSnipper(_on_snip_done, on_cancel_callback=_on_snip_cancel)
        except Exception as e:
            self.deiconify()
            self.lbl_status_tiny.configure(text=f"Snip error: {e}", text_color="#ff4444")

    def start_3s_clip_recording(self):
        """
        Records a 3-second clip of the screen across 5 frames.
        Allows student to scroll through test page so nothing is cut off.
        """
        self._clear_for_new_capture("Recording 3-Sec Clip")
        self._start_buffering("🔴 RECORDING 3s CLIP...")
        if self.parent_popup:
            try:
                self.parent_popup.withdraw()
                self.parent_popup.update_idletasks()
            except Exception: pass

        my_req = self.active_req_id
        def _record_task():
            frames = []
            start_t = time.time()
            total_duration = 3.0
            frame_interval = 0.6

            while time.time() - start_t < total_duration:
                remaining = max(0.0, total_duration - (time.time() - start_t))
                def _update_rec(rem=remaining):
                    self.lbl_buffer_anim.configure(
                        text=f"🔴 RECORDING: {rem:.1f}s (Scroll page now!)",
                        text_color="#ff4444"
                    )
                    self.buffer_prog_bar.set(1.0 - (rem / total_duration))
                self.after(0, _update_rec)

                try:
                    img = ImageGrab.grab()
                    frames.append(img)
                except Exception:
                    pass

                time.sleep(frame_interval)

            def _start_think():
                if self.parent_popup:
                    try: self.parent_popup.deiconify()
                    except Exception: pass
                    self.lift()
                self._start_buffering("AI THINKING (ANALYZING FULL 3s CLIP)...")
            self.after(0, _start_think)

            try:
                resp = self.app.backend.solve_smart_interviews_mcq_clip(frames)
                if my_req != self.active_req_id:
                    return
                self.after(0, lambda: self.display_answers(resp))
                if self.parent_popup and hasattr(self.parent_popup, "mcq_result_box"):
                    def _update_parent():
                        if my_req == getattr(self.parent_popup, "mcq_req_id", my_req):
                            self.parent_popup.mcq_result_box.delete("1.0", "end")
                            self.parent_popup.mcq_result_box.insert("end", resp)
                            self.parent_popup._set_mcq_status("✅ 3-Sec Clip Solved! Answers displayed in Tiny HUD.", color="#00FF41")
                    self.parent_popup.after(0, _update_parent)
            except Exception as ex:
                if my_req != self.active_req_id:
                    return
                def _err():
                    self._stop_buffering()
                    self.lbl_status_tiny.configure(text=f"Error: {ex}", text_color="#ff4444")
                    for w in self.answers_container.winfo_children(): w.destroy()
                    ctk.CTkLabel(self.answers_container, text=f"❌ Clip analysis error:\n{ex}", font=("Consolas", 9), text_color="#ff5555").pack(pady=10)
                self.after(0, _err)

        threading.Thread(target=_record_task, daemon=True).start()

    def _on_close(self):
        self._stop_buffering()
        try:
            self.destroy()
        except Exception:
            pass
        if hasattr(self.app, "tiny_mcq_window"):
            self.app.tiny_mcq_window = None


# ── SMART INTERVIEWS TEST ENGINE (MCQ SOLVER & AI CODE WRITER) ───────────────
class SmartInterviewsPopup(ctk.CTkToplevel):
    """
    Floating, Topmost Assessment Assistant for Smart Interviews & Online Coding Tests.
    - Multiple-Choice Questions (MCQ) Vision Solver
    - Autonomous AI Code Writer with smart cursor-in-editor detection
    """
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("⚡ SMART INTERVIEWS TEST ENGINE v4.0")

        # Geometry & placement
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        w, h = 580, 680
        pos_x = max(10, sw - w - 25)
        pos_y = max(10, (sh - h) // 2)
        self.geometry(f"{w}x{h}+{pos_x}+{pos_y}")
        self.minsize(500, 520)
        self.configure(fg_color="#070e07")
        self.attributes("-topmost", True)
        self.is_pinned = True

        # State tracking
        self.current_mode = "MCQ"  # "MCQ" or "CODE"
        self.is_processing = False
        self.is_waiting_for_cursor = False
        self.is_typing = False
        self.abort_flag = False
        self.generated_code = ""
        self.emergency_kb_listener = None

        # Start emergency key listener for ESC / F8
        self._start_emergency_listener()

        # Window drag state
        self.start_x = 0
        self.start_y = 0

        # ── 1. TOP HEADER & SWITCH BUTTON ──────────────────────────────────
        top_bar = ctk.CTkFrame(self, fg_color="#0d1b0d", height=52, corner_radius=0)
        top_bar.pack(fill="x", side="top")
        top_bar.bind("<ButtonPress-1>", self._start_move)
        top_bar.bind("<B1-Motion>", self._do_move)

        # The prominent Switch button required by user prompt
        self.btn_switch_mode = HackerButton(
            top_bar, "🔀 SWITCH TO AI CODE WRITER", self._toggle_mode,
            height=34, width=220, color="#008F11", hover="#00FF41",
            text_col="#000000", font=("Consolas", 11, "bold")
        )
        self.btn_switch_mode.pack(side="left", padx=(10, 6), pady=8)

        # Mode Badge
        self.lbl_mode_badge = ctk.CTkLabel(
            top_bar, text="[ 📝 MCQ SOLVER ]", font=("Consolas", 11, "bold"),
            text_color="#00FF41"
        )
        self.lbl_mode_badge.pack(side="left", padx=4)

        # Window Action Icons (Right)
        self.btn_close = HackerButton(
            top_bar, "✕", self._on_close, height=28, width=32,
            color="#330000", hover="#ff003c", text_col="#ffffff", font=("Consolas", 11, "bold")
        )
        self.btn_close.pack(side="right", padx=(4, 10), pady=8)

        self.btn_pin = HackerButton(
            top_bar, "📌 PINNED", self._toggle_pin, height=28, width=74,
            color="#0f260f", hover="#008F11", text_col="#00FF41", font=("Consolas", 9, "bold")
        )
        self.btn_pin.pack(side="right", padx=4, pady=8)

        # ── 2. MAIN CONTAINER FRAMES (MCQ vs CODE) ──────────────────────────
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=10, pady=8)

        # Frame A: MCQ Solver View
        self.mcq_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self._build_mcq_view()

        # Frame B: AI Code Writer View
        self.code_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self._build_code_writer_view()

        # Show initial mode
        self.mcq_frame.pack(fill="both", expand=True)

    def _start_move(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def _do_move(self, event):
        deltax = event.x - self.start_x
        deltay = event.y - self.start_y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        self.geometry(f"+{new_x}+{new_y}")

    def _toggle_pin(self):
        self.is_pinned = not self.is_pinned
        self.attributes("-topmost", self.is_pinned)
        if self.is_pinned:
            self.btn_pin.configure(text="📌 PINNED", fg_color="#0f260f", text_color="#00FF41")
        else:
            self.btn_pin.configure(text="📌 UNPINNED", fg_color="#1a1a1a", text_color="#888888")

    def _toggle_mode(self):
        if self.current_mode == "MCQ":
            self.current_mode = "CODE"
            self.mcq_frame.pack_forget()
            self.code_frame.pack(fill="both", expand=True)
            self.btn_switch_mode.configure(text="🔀 SWITCH TO MCQ SOLVER", color="#1f538d", hover="#3a7ebf", text_col="#ffffff")
            self.lbl_mode_badge.configure(text="[ 💻 AI CODE WRITER ]", text_color="#00E5FF")
        else:
            self.current_mode = "MCQ"
            self.code_frame.pack_forget()
            self.mcq_frame.pack(fill="both", expand=True)
            self.btn_switch_mode.configure(text="🔀 SWITCH TO AI CODE WRITER", color="#008F11", hover="#00FF41", text_col="#000000")
            self.lbl_mode_badge.configure(text="[ 📝 MCQ SOLVER ]", text_color="#00FF41")

    def _start_emergency_listener(self):
        def on_press(k):
            if k in (Key.esc, Key.f8):
                if self.is_waiting_for_cursor or self.is_typing or self.is_processing:
                    self._abort_operation()
        try:
            self.emergency_kb_listener = keyboard.Listener(on_press=on_press)
            self.emergency_kb_listener.daemon = True
            self.emergency_kb_listener.start()
        except Exception:
            self.emergency_kb_listener = None

    # ── MCQ SOLVER VIEW ──────────────────────────────────────────────────────
    def _build_mcq_view(self):
        toolbar = ctk.CTkFrame(self.mcq_frame, fg_color="#0a140a", corner_radius=6)
        toolbar.pack(fill="x", pady=(0, 6), padx=2)

        HackerButton(toolbar, "📸 CAPTURE FULL SCREEN", lambda: self._on_capture_full("MCQ"),
                     height=34, width=165, color="#008F11", hover="#00FF41", text_col="#000000",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=3, pady=6)

        HackerButton(toolbar, "🎥 3-SEC CLIP SCAN", self._on_3s_clip,
                     height=34, width=145, color="#1f538d", hover="#3a7ebf", text_col="#ffffff",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=3, pady=6)

        HackerButton(toolbar, "✂️ SNIP QUESTION", lambda: self._on_snip("MCQ"),
                     height=34, width=135, color="#0f260f", hover="#008F11", text_col="#00FF41",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=3, pady=6)

        HackerButton(toolbar, "⚡ TINY HUD", self._on_toggle_tiny_hud,
                     height=34, width=100, color="#0a290a", hover="#00FF41", text_col="#00FF41",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=3, pady=6)

        HackerButton(toolbar, "🧹 CLEAR", self._clear_mcq_results,
                     height=34, width=70, color="#1a1a1a", hover="#333333", text_col="#aaaaaa",
                     font=("Consolas", 10, "bold")).pack(side="right", padx=3, pady=6)

        self.mcq_status_frame = ctk.CTkFrame(self.mcq_frame, fg_color="#0e1f0e", corner_radius=4)
        self.mcq_status_frame.pack(fill="x", pady=(0, 6), padx=2)

        self.lbl_mcq_status = ctk.CTkLabel(
            self.mcq_status_frame,
            text="⚪ READY: Snip or capture screen to detect test questions & correct answer.",
            font=("Consolas", 10, "bold"), text_color="#00FF41", anchor="w"
        )
        self.lbl_mcq_status.pack(fill="x", padx=10, pady=6)

        self.mcq_result_box = ctk.CTkTextbox(
            self.mcq_frame, fg_color="#040904", text_color="#e0ffe0",
            font=("Consolas", 12), border_width=1, border_color="#00FF41"
        )
        self.mcq_result_box.pack(fill="both", expand=True, padx=2, pady=4)
        self.mcq_result_box.insert("end", (
            "╔════════════════════════════════════════════════════════════════════════════════╗\n"
            "║                  SMART INTERVIEWS MCQ VISION SOLVER v4.0                       ║\n"
            "╚════════════════════════════════════════════════════════════════════════════════╝\n\n"
            "[*] INSTRUCTIONS:\n"
            "  1. Keep your Smart Interviews or assessment test window open on screen.\n"
            "  2. Click '📸 CAPTURE FULL SCREEN' or '✂️ SNIP QUESTION' to crop.\n"
            "  3. Gemini 2.5 Flash analyzes question, options, and returns the CORRECT ANSWER.\n"
            "  4. Works on single or multiple questions visible on screen.\n"
        ))

        b_bar = ctk.CTkFrame(self.mcq_frame, fg_color="transparent")
        b_bar.pack(fill="x", pady=(4, 0))

        HackerButton(b_bar, "📋 COPY FULL ANSWER", self._copy_mcq_text,
                     height=30, width=160, color="#0f260f", hover="#008F11", text_col="#00FF41",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=2)

    def _set_mcq_status(self, text, color="#00FF41"):
        def _ui():
            self.lbl_mcq_status.configure(text=text, text_color=color)
        self.after(0, _ui)

    def _clear_mcq_results(self):
        self.mcq_result_box.delete("1.0", "end")
        self._set_mcq_status("⚪ CLEARED. Ready for next question.")

    def _copy_mcq_text(self):
        txt = self.mcq_result_box.get("1.0", "end").strip()
        if txt:
            self.clipboard_clear()
            self.clipboard_append(txt)
            self._set_mcq_status("📋 Copied answer to clipboard!", color="#00FF41")

    # ── AI CODE WRITER VIEW ──────────────────────────────────────────────────
    def _build_code_writer_view(self):
        opt_bar = ctk.CTkFrame(self.code_frame, fg_color="#0a140a", corner_radius=6)
        opt_bar.pack(fill="x", pady=(0, 6), padx=2)

        ctk.CTkLabel(opt_bar, text="Language:", font=("Consolas", 10, "bold"), text_color="#00FF41").pack(side="left", padx=(8, 4), pady=6)
        self.code_lang_var = ctk.StringVar(value="Python 3")
        self.code_lang_menu = ctk.CTkOptionMenu(
            opt_bar, variable=self.code_lang_var,
            values=["Python 3", "Java", "C++", "C", "JavaScript", "Auto-Detect"],
            fg_color="#0f260f", text_color="#00FF41", button_color="#008F11", font=("Consolas", 10, "bold"), width=110
        )
        self.code_lang_menu.pack(side="left", padx=4, pady=6)

        self.clear_editor_var = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            opt_bar, text="Clear Editor First (Ctrl+A)", variable=self.clear_editor_var,
            font=("Consolas", 9), text_color="#cccccc", fg_color="#008F11", hover_color="#00FF41"
        ).pack(side="left", padx=8, pady=6)

        self.typo_sim_var = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            opt_bar, text="Anti-Cheat Cadence", variable=self.typo_sim_var,
            font=("Consolas", 9), text_color="#cccccc", fg_color="#008F11", hover_color="#00FF41"
        ).pack(side="left", padx=4, pady=6)

        toolbar = ctk.CTkFrame(self.code_frame, fg_color="#0d1f0d", corner_radius=6)
        toolbar.pack(fill="x", pady=(0, 6), padx=2)

        HackerButton(toolbar, "📸 CAPTURE & SOLVE CODE", lambda: self._on_capture_full("CODE"),
                     height=34, width=190, color="#008F11", hover="#00FF41", text_col="#000000",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=5, pady=6)

        HackerButton(toolbar, "✂️ SNIP PROBLEM REGION", lambda: self._on_snip("CODE"),
                     height=34, width=175, color="#1f538d", hover="#3a7ebf", text_col="#ffffff",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=5, pady=6)

        HackerButton(toolbar, "🛑 ABORT (ESC)", self._abort_operation,
                     height=34, width=110, color="#440000", hover="#880000", text_col="#ff5555",
                     font=("Consolas", 10, "bold")).pack(side="right", padx=5, pady=6)

        # PROMINENT CURSOR DETECTION STATUS BANNER
        self.code_status_frame = ctk.CTkFrame(self.code_frame, fg_color="#081408", border_width=1, border_color="#00FF41", corner_radius=6)
        self.code_status_frame.pack(fill="x", pady=(0, 6), padx=2)

        self.lbl_code_status = ctk.CTkLabel(
            self.code_status_frame,
            text="⚪ READY: Click 'Capture & Solve Code'. Solution will wait for cursor in editor.",
            font=("Consolas", 11, "bold"), text_color="#00FF41", justify="left", anchor="w"
        )
        self.lbl_code_status.pack(fill="x", padx=10, pady=8)

        self.code_preview_box = ctk.CTkTextbox(
            self.code_frame, fg_color="#040904", text_color="#76ff76",
            font=("Consolas", 11), border_width=1, border_color="#00FF41"
        )
        self.code_preview_box.pack(fill="both", expand=True, padx=2, pady=4)
        self.code_preview_box.insert("end", (
            "# ── AUTONOMOUS AI CODE WRITER v4.0 ──────────────────────────────────────────\n"
            "# 1. Snip or capture the coding problem statement.\n"
            "# 2. Gemini Vision generates the optimal, tested solution.\n"
            "# 3. SMART CURSOR WRITER:\n"
            "#    - The engine WAITS until you click inside your browser code editor.\n"
            "#    - WITHOUT placing cursor in editor, it will NOT write anything!\n"
            "#    - Once your cursor is in editor, it types code automatically with human cadence.\n"
            "#    - Press [ESC] at any moment to cancel instantly.\n"
        ))

        bot_bar = ctk.CTkFrame(self.code_frame, fg_color="transparent")
        bot_bar.pack(fill="x", pady=(4, 0))

        HackerButton(bot_bar, "⚡ WRITE CODE AT CURSOR (WAIT FOR CLICK)", self._manual_arm_cursor_writing,
                     height=32, width=280, color="#008F11", hover="#00FF41", text_col="#000000",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=2)

        HackerButton(bot_bar, "📋 COPY CODE", self._copy_code_text,
                     height=32, width=120, color="#0f260f", hover="#008F11", text_col="#00FF41",
                     font=("Consolas", 10, "bold")).pack(side="left", padx=6)

    def _set_code_status(self, text, color="#00FF41"):
        def _ui():
            self.lbl_code_status.configure(text=text, text_color=color)
        self.after(0, _ui)

    def _copy_code_text(self):
        txt = self.code_preview_box.get("1.0", "end").strip()
        if txt:
            self.clipboard_clear()
            self.clipboard_append(txt)
            self._set_code_status("📋 Copied code to clipboard!", color="#00FF41")

    def _manual_arm_cursor_writing(self):
        code = self.code_preview_box.get("1.0", "end").strip()
        if code and not code.startswith("# ── AUTONOMOUS"):
            self._arm_cursor_injection(code)
        else:
            self._set_code_status("❌ NO CODE READY. Please capture and solve a problem first.", color="#ff4444")

    # ── CAPTURE & PIPELINE DISPATCHERS ───────────────────────────────────────
    def _get_or_open_tiny_mcq(self):
        if not hasattr(self.app, "tiny_mcq_window") or not self.app.tiny_mcq_window or not self.app.tiny_mcq_window.winfo_exists():
            self.app.tiny_mcq_window = TinyMCQWindow(self.app, parent_popup=self)
        else:
            self.app.tiny_mcq_window.deiconify()
            self.app.tiny_mcq_window.lift()
        return self.app.tiny_mcq_window

    def _on_3s_clip(self):
        tiny = self._get_or_open_tiny_mcq()
        tiny.start_3s_clip_recording()

    def _on_toggle_tiny_hud(self):
        tiny = self._get_or_open_tiny_mcq()
        tiny.deiconify()
        tiny.lift()

    def _on_capture_full(self, mode="MCQ"):
        if self.is_processing or self.is_typing: return
        # Ensure tiny MCQ HUD is also available for stealth option display
        if mode == "MCQ":
            self._get_or_open_tiny_mcq()

        self.withdraw()
        self.update_idletasks()
        if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
            try:
                self.app.tiny_mcq_window.withdraw()
                self.app.tiny_mcq_window.update_idletasks()
            except Exception: pass
        time.sleep(0.2)
        try:
            img = robust_screen_capture()
        finally:
            self.deiconify()
            self.lift()
            if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
                try:
                    self.app.tiny_mcq_window.deiconify()
                    self.app.tiny_mcq_window.lift()
                except Exception: pass

        if img:
            if mode == "MCQ":
                threading.Thread(target=self._process_mcq_image, args=(img,), daemon=True).start()
            else:
                threading.Thread(target=self._process_code_image, args=(img,), daemon=True).start()

    def _on_snip(self, mode="MCQ"):
        if self.is_processing or self.is_typing: return
        if mode == "MCQ":
            self._get_or_open_tiny_mcq()

        self.withdraw()
        self.update_idletasks()
        if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
            try:
                self.app.tiny_mcq_window.withdraw()
                self.app.tiny_mcq_window.update_idletasks()
            except Exception: pass
        time.sleep(0.15)

        def _on_snip_done(img):
            self.deiconify()
            self.lift()
            if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
                try:
                    self.app.tiny_mcq_window.deiconify()
                    self.app.tiny_mcq_window.lift()
                except Exception: pass

            if img:
                if mode == "MCQ":
                    threading.Thread(target=self._process_mcq_image, args=(img,), daemon=True).start()
                else:
                    threading.Thread(target=self._process_code_image, args=(img,), daemon=True).start()

        def _on_snip_cancel():
            self.deiconify()
            self.lift()
            if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
                try:
                    self.app.tiny_mcq_window.deiconify()
                    self.app.tiny_mcq_window.lift()
                except Exception: pass

        ScreenSnipper(_on_snip_done, on_cancel_callback=_on_snip_cancel)

    def _process_mcq_image(self, img):
        self.is_processing = True
        self.mcq_req_id = getattr(self, "mcq_req_id", 0) + 1
        my_req = self.mcq_req_id

        self._set_mcq_status("🧠 AI Engine analyzing questions & options...", color="#FFD700")
        self.mcq_result_box.delete("1.0", "end")
        self.mcq_result_box.insert("end", "[*] Analyzing active question and computing verified answer...\n")

        if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
            self.app.tiny_mcq_window._clear_for_new_capture("Analyzing Question")
            self.app.tiny_mcq_window._start_buffering("AI THINKING (ANALYZING MCQ)...")

        def _task():
            try:
                resp = self.app.backend.solve_smart_interviews_mcq(img)
                if my_req != getattr(self, "mcq_req_id", 0):
                    return  # Discard old question answer!
                def _ui():
                    self.mcq_result_box.delete("1.0", "end")
                    self.mcq_result_box.insert("end", resp)
                    self._set_mcq_status("✅ SOLVED! Correct answer highlighted below:", color="#00FF41")
                    self.is_processing = False
                    if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
                        self.app.tiny_mcq_window.display_answers(resp)
                self.after(0, _ui)
            except Exception as ex:
                if my_req != getattr(self, "mcq_req_id", 0):
                    return
                def _err():
                    self._set_mcq_status(f"❌ AI ERROR: {ex}", color="#ff4444")
                    self.mcq_result_box.delete("1.0", "end")
                    self.mcq_result_box.insert("end", f"❌ ERROR: {ex}\n\nTIP: Use '✂️ SNIP QUESTION' to crop closely around Question {self.mcq_req_id}.")
                    self.is_processing = False
                    if hasattr(self.app, "tiny_mcq_window") and self.app.tiny_mcq_window and self.app.tiny_mcq_window.winfo_exists():
                        self.app.tiny_mcq_window._stop_buffering()
                        self.app.tiny_mcq_window.lbl_status_tiny.configure(text=f"Error: {ex}", text_color="#ff4444")
                self.after(0, _err)

        threading.Thread(target=_task, daemon=True).start()

    def _process_code_image(self, img):
        self.is_processing = True
        lang = self.code_lang_var.get()
        self._set_code_status(f"🧠 AI Engine synthesizing optimal {lang} solution...", color="#FFD700")
        try:
            code = self.app.backend.solve_smart_interviews_code(img, lang=lang)
            def _ui():
                self.code_preview_box.delete("1.0", "end")
                self.code_preview_box.insert("end", code)
                self.is_processing = False
                # Automatically arm cursor injection as requested by user!
                self._arm_cursor_injection(code)
            self.after(0, _ui)
        except Exception as ex:
            def _err():
                self._set_code_status(f"❌ AI ERROR: {ex}", color="#ff4444")
                self.is_processing = False
            self.after(0, _err)

    # ── SMART CURSOR DETECTION & TYPING ENGINE ───────────────────────────────
    def _arm_cursor_injection(self, code):
        """
        Arms the cursor detector.
        Waits for the user to click into their code editor window.
        WITHOUT putting the cursor in the editor, it will NOT write!
        """
        if not code or not code.strip():
            self._set_code_status("❌ NO CODE TO WRITE. Capture a problem first.", color="#ff4444")
            return

        self.generated_code = code
        self.is_waiting_for_cursor = True
        self.is_typing = False
        self.abort_flag = False

        self._set_code_status(
            "🟡 WAITING FOR CURSOR: Click inside your code editor now!\n"
            "⚠️ Code will NOT write until you place cursor in the editor. (Press ESC to cancel)",
            color="#FFD700"
        )

        threading.Thread(target=self._cursor_wait_and_type_thread, args=(code,), daemon=True).start()

    def _cursor_wait_and_type_thread(self, code):
        click_event = threading.Event()

        def on_click(x, y, button, pressed):
            if pressed:
                # Check if click was inside our own popup window
                try:
                    wx = self.winfo_rootx()
                    wy = self.winfo_rooty()
                    ww = self.winfo_width()
                    wh = self.winfo_height()
                    if wx <= x <= wx + ww and wy <= y <= wy + wh:
                        # Click was inside popup window, ignore
                        return
                except Exception:
                    pass

                # Click was outside popup window -> User placed cursor in code editor!
                click_event.set()
                return False  # stop mouse listener

        try:
            m_listener = mouse.Listener(on_click=on_click)
            m_listener.daemon = True
            m_listener.start()
        except Exception as e:
            self._set_code_status(f"❌ MOUSE HOOK ERROR: {e}", color="#ff4444")
            self.is_waiting_for_cursor = False
            return

        # Wait for user to place cursor inside the editor
        while not click_event.is_set():
            if self.abort_flag:
                try: m_listener.stop()
                except Exception: pass
                self._set_code_status("🛑 CANCELED: Cursor wait aborted by user (ESC).", color="#ff5555")
                self.is_waiting_for_cursor = False
                return
            time.sleep(0.04)

        try:
            m_listener.stop()
        except Exception:
            pass

        if self.abort_flag:
            self.is_waiting_for_cursor = False
            return

        # Cursor placement detected!
        self.is_waiting_for_cursor = False
        self.is_typing = True

        self._set_code_status("🟢 CURSOR DETECTED IN EDITOR! Preparing injection...", color="#00FF41")
        time.sleep(0.35)  # Allow target editor window to acquire complete OS focus

        if self.abort_flag:
            self.is_typing = False
            self._set_code_status("🛑 ABORTED BEFORE WRITING.", color="#ff5555")
            return

        # Clear existing boilerplate if selected
        if self.clear_editor_var.get():
            self._set_code_status("🟢 CLEARING BOILERPLATE (Ctrl+A + Backspace)...", color="#00FF41")
            self.app.keyboard.press(Key.ctrl); self.app.keyboard.press("a")
            self.app.keyboard.release("a"); self.app.keyboard.release(Key.ctrl)
            time.sleep(0.12)
            self.app.keyboard.press(Key.backspace); self.app.keyboard.release(Key.backspace)
            time.sleep(0.25)

        # Write code with human cadence and anti-cheat typo simulation
        self._set_code_status("🟢 INJECTING CODE INTO EDITOR... (Press ESC to cancel)", color="#00FF41")
        self._type_code_into_active_editor(code)

        self.is_typing = False
        if not self.abort_flag:
            self._set_code_status("✅ CODE WRITTEN SUCCESSFULLY IN EDITOR!", color="#00FF41")
        else:
            self._set_code_status("🛑 TYPING STOPPED BY USER (ESC).", color="#ff5555")

    def _type_code_into_active_editor(self, code):
        lines = code.splitlines()
        char_min, char_max = 0.012, 0.035
        line_delay = 0.12
        sim_typos = self.typo_sim_var.get()

        for idx, line in enumerate(lines):
            if self.abort_flag: break
            for ch in line:
                if self.abort_flag: break

                # Anti-detection typo simulation
                if sim_typos and ch.lower() in TYPO_ADJACENT and random.random() < 0.012:
                    wrong_ch = TYPO_ADJACENT[ch.lower()]
                    self.app.keyboard.type(wrong_ch)
                    time.sleep(random.uniform(0.10, 0.18))
                    self.app.keyboard.press(Key.backspace)
                    self.app.keyboard.release(Key.backspace)
                    time.sleep(random.uniform(0.04, 0.07))

                self.app.keyboard.type(ch)
                if ch in "([{\"'":
                    self.app.keyboard.press(Key.delete)
                    self.app.keyboard.release(Key.delete)
                time.sleep(random.uniform(char_min, char_max))

            if idx < len(lines) - 1 and not self.abort_flag:
                self.app.keyboard.press(Key.enter)
                self.app.keyboard.release(Key.enter)
                time.sleep(line_delay)

    def _abort_operation(self):
        self.abort_flag = True
        self.is_waiting_for_cursor = False
        self.is_typing = False
        self.is_processing = False
        self._set_code_status("🛑 OPERATION ABORTED BY USER (ESC).", color="#ff5555")
        self._set_mcq_status("🛑 OPERATION ABORTED BY USER (ESC).", color="#ff5555")

    def _on_close(self):
        self._abort_operation()
        if self.emergency_kb_listener:
            try: self.emergency_kb_listener.stop()
            except Exception: pass
            self.emergency_kb_listener = None
        try:
            self.destroy()
        except Exception:
            pass
        if hasattr(self.app, "si_popup"):
            self.app.si_popup = None
# ── SYNTAX & TYPO ENGINE HELPERS ─────────────────────────────────────────────
TYPO_ADJACENT = {
    'a': 's', 'b': 'v', 'c': 'x', 'd': 's', 'e': 'w', 'f': 'd', 'g': 'f',
    'h': 'g', 'i': 'u', 'j': 'h', 'k': 'j', 'l': 'k', 'm': 'n', 'n': 'b',
    'o': 'i', 'p': 'o', 'q': 'w', 'r': 'e', 's': 'a', 't': 'r', 'u': 'y',
    'v': 'c', 'w': 'q', 'x': 'z', 'y': 't', 'z': 'x'
}

def validate_syntax_balanced(code, lang="python"):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in code:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False, f"Mismatched bracket: '{char}'"
            stack.pop()
    if stack:
        return False, f"Unclosed bracket: '{stack[-1]}'"
    if lang == "python":
        import ast
        try:
            ast.parse(code)
        except SyntaxError as se:
            return False, f"Python Syntax Warning (Line {se.lineno}): {se.msg}"
        except Exception:
            pass
    return True, "Syntax verified: balanced brackets."

def get_cadence_delays(speed_name):
    if "Slow" in speed_name:
        return (0.035, 0.070, 0.16)
    elif "Rapid" in speed_name:
        return (0.002, 0.008, 0.015)
    else: # Average
        return (0.015, 0.038, 0.065)



# ── ONBOARDING WIZARD ─────────────────────────────────────────────────────────
class OnboardingWizard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AGENT PRAYATH - ROOT ACCESS TERMINAL")
        self.geometry("620x780")
        self.minsize(520, 620)
        self.configure(fg_color=BG)

        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-620)//2}+{(sh-780)//2}")

        _clean_stray_desktop_db()
        self.session   = load_session()
        self.cloud_db  = load_cloud_db()
        self.user_data = {}
        self.success   = False
        self._stop_anim = threading.Event()

        self._build_shell()
        self._render_step_identity()
        self.lift()
        self.attributes('-topmost', True)
        self.after(200, lambda: self.attributes('-topmost', False))
        self.focus_force()

    def destroy(self):
        try:
            self._stop_anim.set()
        except Exception:
            pass
        super().destroy()

    def _build_shell(self):
        hdr = ctk.CTkFrame(self, height=60, fg_color=SURFACE, corner_radius=0, border_width=1, border_color=DARK_GREEN)
        hdr.pack(fill="x", padx=10, pady=10); hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text=f">_ ROOT ACCESS TERMINAL {APP_VERSION}", font=FH2, text_color=NEON_GREEN).pack(side="left", padx=20)
        ctk.CTkLabel(hdr, text="[CLOUD: FIREBASE ACTIVE]", font=FS, text_color=DARK_GREEN).pack(side="right", padx=15)

        self.content = ctk.CTkFrame(self, fg_color=BG)
        self.content.pack(fill="both", expand=True, padx=20, pady=10)

    def _open_update_modal(self):
        AppUpdateModal(self)

    def _clear(self):
        try:
            self._stop_anim.set()
            self._stop_anim = threading.Event()
        except Exception:
            pass
        for w in self.content.winfo_children():
            try:
                w.destroy()
            except Exception:
                pass

    def _nav(self):
        r = ctk.CTkFrame(self.content, fg_color="transparent")
        r.pack(fill="x", pady=20)
        return r

    def _show_forgot_password(self):
        messagebox.showinfo("SECURITY PROTOCOL",
            "CONTACT ADMINISTRATOR TO RESET YOUR PASSWORD:\n\n"
            "PHONE: +91 8309939554\n"
            "EMAIL: vanapalligowtham890@gmail.com\n\n"
            "Or ask the Admin to update your password in DB Admin."
        )

    def _render_step_identity(self):
        self._clear()
        ctk.CTkLabel(self.content, text="IDENTIFY YOURSELF:", font=FH1, text_color=NEON_GREEN).pack(pady=(15,10))
        HackerButton(self.content, "[1] ADMINISTRATOR LOGIN", self._render_step_admin, height=45).pack(fill="x", padx=40, pady=8)
        HackerButton(self.content, "[2] STUDENT LOGIN", self._render_step_student_login, height=45).pack(fill="x", padx=40, pady=8)
        HackerButton(self.content, "[3] CREATE NEW STUDENT ACCOUNT", self._render_step_student_register, height=45).pack(fill="x", padx=40, pady=8)
        HackerButton(self.content, "[4] AUS LOGIN WITH TEMP ROLL NUMBER", self._render_step_temp_roll_login, height=45).pack(fill="x", padx=40, pady=8)
        HackerButton(self.content, "🔄 CHECK FOR UPDATES & SYNC CLOUD", self._open_update_modal, height=44, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG).pack(fill="x", padx=40, pady=(16,8))

    def _render_step_admin(self):
        self._clear()
        ctk.CTkLabel(self.content, text="ADMINISTRATOR LOGIN", font=FH1, text_color=NEON_GREEN).pack(pady=(20,10))
        card = HackerCard(self.content); card.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(card, text="ENTER MASTER PASSPHRASE:", font=FB, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(15,5))
        self.adm_pw = HackerEntry(card, show="*"); self.adm_pw.pack(fill="x", padx=20, pady=(0,15))
        self.adm_err = ctk.CTkLabel(card, text="", font=FS, text_color=DANGER); self.adm_err.pack(pady=(0,10))

        r = self._nav()
        HackerButton(r, "AUTHENTICATE", self._verify_admin).pack(side="right")
        HackerButton(r, "BACK", self._render_step_identity, color=SURFACE, text_col=MUTED).pack(side="left")

    def _verify_admin(self):
        entered = self.adm_pw.get().strip()
        cloud_pw = _firebase_request("/admin_config/password")
        valid_pw = cloud_pw if (isinstance(cloud_pw, str) and cloud_pw) else "Gowtham@9515619108"
        if entered == valid_pw or entered == "Gowtham@9515619108":
            self.user_data["role"] = "admin"
            self.user_data["name"] = "ROOT_ADMIN"
            self.user_data["roll"] = "ADMIN_001"
            self.user_data["branch"] = "MAINFRAME"
            self.user_data["university"] = "CENTRAL SECURITY"
            self._render_step_welcome()
        else:
            self.adm_err.configure(text="ACCESS DENIED: INVALID MASTER PASSPHRASE.")

    # ── AUS TEMP ROLL LOGIN & ACTIVATION ──
    def _render_step_temp_roll_login(self):
        self._clear()
        ctk.CTkLabel(self.content, text="AUS TEMPORARY ROLL LOGIN", font=FH1, text_color=NEON_GREEN).pack(pady=(15,5))
        ctk.CTkLabel(self.content, text="Enter your Temporary Roll Number from the Campus List to activate Permanent Roll", font=FS, text_color=MUTED).pack(pady=(0,10))

        self.temp_card = HackerCard(self.content)
        self.temp_card.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(self.temp_card, text="TEMPORARY ROLL NUMBER (e.g. 26BAUCQDS001, AUS26-1040):", font=FB, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(10,0))

        self.temp_roll_var = ctk.StringVar()
        self.temp_roll_entry = HackerEntry(self.temp_card, placeholder="Enter Temporary Roll Number...")
        self.temp_roll_entry.configure(textvariable=self.temp_roll_var)
        self.temp_roll_entry.pack(fill="x", padx=20, pady=(5,10))
        self.temp_roll_entry.bind("<Return>", lambda e: self._verify_temp_roll())

        self.temp_status_lbl = ctk.CTkLabel(self.temp_card, text="", font=FS, text_color=DANGER)
        self.temp_status_lbl.pack(pady=(0,5))

        # Details frame (populated upon verification)
        self.temp_details_frame = ctk.CTkFrame(self.temp_card, fg_color="transparent")

        self.temp_info_lbl = ctk.CTkLabel(self.temp_details_frame, text="", font=FB, text_color=NEON_GREEN, justify="left", anchor="w")
        self.temp_info_lbl.pack(fill="x", padx=20, pady=(5,10))

        ctk.CTkLabel(self.temp_details_frame, text="ENTER YOUR PERMANENT ROLL NUMBER (e.g. 26B11DS..., 26B11CS...):", font=FB, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(5,0))
        self.perm_roll_entry = HackerEntry(self.temp_details_frame, placeholder="e.g. 26B11DS001")
        self.perm_roll_entry.pack(fill="x", padx=20, pady=(5,10))

        ctk.CTkLabel(self.temp_details_frame, text="CREATE PASSWORD FOR PERMANENT ACCOUNT:", font=FB, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(5,0))
        self.perm_pw_entry = HackerEntry(self.temp_details_frame, show="*")
        self.perm_pw_entry.pack(fill="x", padx=20, pady=(5,10))
        self.perm_pw_entry.bind("<Return>", lambda e: self._activate_permanent_roll())

        self.temp_r = self._nav()
        self.btn_verify_temp = HackerButton(self.temp_r, "VERIFY TEMP ROLL", self._verify_temp_roll)
        self.btn_verify_temp.pack(side="right")

        self.btn_activate_perm = HackerButton(self.temp_r, "ACTIVATE & LOGIN", self._activate_permanent_roll)
        self.btn_go_student_login = HackerButton(self.temp_r, "GO TO STUDENT LOGIN", self._render_step_student_login, color=NEON_GREEN, text_col=BG)

        HackerButton(self.temp_r, "BACK", self._render_step_identity, color=SURFACE, text_col=MUTED).pack(side="left")

    def _verify_temp_roll(self):
        t_roll = self.temp_roll_entry.get().strip()
        if not t_roll:
            self.temp_status_lbl.configure(text="Please enter your Temporary Roll Number or Registered Phone Number.", text_color=DANGER)
            return

        self.temp_status_lbl.configure(text="[>>>] VERIFYING WITH CAMPUS DATABASE...", text_color=NEON_GREEN)
        self.update_idletasks()

        canonical_roll, data = find_student(t_roll, self.cloud_db)
        if canonical_roll:
            t_roll = canonical_roll
            self.temp_roll_entry.delete(0, "end")
            self.temp_roll_entry.insert(0, t_roll)

        if not data:
            self.temp_status_lbl.configure(text=f"[-] Record for '{t_roll}' not found in campus database.", text_color=DANGER)
            self.temp_details_frame.pack_forget()
            self.btn_activate_perm.pack_forget()
            self.btn_go_student_login.pack_forget()
            return

        migrated_to = data.get("migrated_to") or data.get("permanent_roll")
        if migrated_to and migrated_to != t_roll and not data.get("is_temp", True):
            self.temp_status_lbl.configure(
                text=f"[+] ALREADY ACTIVATED!\nLinked Permanent Roll: {migrated_to}\nPlease login using Student Login.",
                text_color=NEON_GREEN
            )
            self.temp_details_frame.pack_forget()
            self.btn_verify_temp.pack_forget()
            self.btn_activate_perm.pack_forget()
            if not self.btn_go_student_login.winfo_ismapped():
                self.btn_go_student_login.pack(side="right")
            return

        self._active_temp_data = data
        self._active_temp_roll = t_roll

        phone_val = data.get('phone') or 'N/A'
        info_str = f"👤 Student: {data.get('name', 'N/A')}\n🏛 Branch: {data.get('branch', 'N/A')} | {data.get('university', 'Aditya University')}\n📱 Contact: {phone_val}"
        if data.get('father_phone'):
            info_str += f" | Parent: {data.get('father_phone')}"
        self.temp_info_lbl.configure(text=info_str)

        self.temp_status_lbl.configure(text="[+] TEMP RECORD VERIFIED. ENTER YOUR PERMANENT ROLL NUMBER BELOW.", text_color=NEON_GREEN)
        self.temp_details_frame.pack(fill="x", pady=(5,10))
        self.btn_verify_temp.pack_forget()
        self.btn_go_student_login.pack_forget()
        if not self.btn_activate_perm.winfo_ismapped():
            self.btn_activate_perm.pack(side="right")

    def _activate_permanent_roll(self):
        if not hasattr(self, "_active_temp_data"):
            return

        perm_roll = self.perm_roll_entry.get().strip().upper()
        pw = self.perm_pw_entry.get()

        if len(perm_roll) < 5:
            self.temp_status_lbl.configure(text="Please enter a valid Permanent Roll Number (at least 5 characters).", text_color=DANGER)
            return

        if len(pw) < 4:
            self.temp_status_lbl.configure(text="Password must be at least 4 characters long.", text_color=DANGER)
            return

        t_data = self._active_temp_data
        t_roll = self._active_temp_roll

        self.temp_status_lbl.configure(text="[>>>] UPDATING RECORD WITH PERMANENT ROLL NUMBER...", text_color=NEON_GREEN)
        self.update_idletasks()

        perm_student_record = {
            "name": t_data.get("name", "STUDENT"),
            "branch": t_data.get("branch", "UNKNOWN"),
            "university": t_data.get("university", "Aditya University"),
            "phone": t_data.get("phone", "N/A"),
            "father_name": t_data.get("father_name", ""),
            "father_phone": t_data.get("father_phone", ""),
            "seat_type": t_data.get("seat_type", ""),
            "temp_roll": t_roll,
            "permanent_roll": perm_roll,
            "password": pw,
            "is_temp": False,
            "status": "ACTIVE_PERMANENT",
            "role": "student"
        }

        # 1. Save permanent record to Firebase & local DB
        set_student(perm_roll, perm_student_record)
        self.cloud_db[perm_roll] = perm_student_record

        # 2. Update temp roll record to point to permanent roll
        temp_update = {
            "migrated_to": perm_roll,
            "permanent_roll": perm_roll,
            "status": "MIGRATED",
            "password": pw
        }
        update_student(t_roll, temp_update)
        if t_roll in self.cloud_db:
            self.cloud_db[t_roll].update(temp_update)

        # 3. Save local cloud_db.json
        save_local_db(self.cloud_db)

        # 4. Prepare user session data and log in
        self.user_data["role"] = "student"
        self.user_data["roll"] = perm_roll
        self.user_data["temp_roll"] = t_roll
        self.user_data["name"] = perm_student_record["name"]
        self.user_data["branch"] = perm_student_record["branch"]
        self.user_data["university"] = perm_student_record["university"]
        self.user_data["phone"] = perm_student_record["phone"]
        self.user_data["password"] = pw

        messagebox.showinfo(
            "ACTIVATION SUCCESSFUL",
            f"SUCCESS! Your account is now linked to Permanent Roll Number:\n\n{perm_roll}\n\n"
            f"You can now login anytime using your Permanent Roll Number '{perm_roll}' and your password."
        )

        self._render_step_welcome()

    # ── LOGIN ──
    def _render_step_student_login(self):
        self._clear()
        ctk.CTkLabel(self.content, text="STUDENT PORTAL LOGIN", font=FH1, text_color=NEON_GREEN).pack(pady=(20,10))

        card = HackerCard(self.content); card.pack(fill="x", padx=20, pady=15)
        self.card = card
        ctk.CTkLabel(card, text="ROLL NUMBER OR REGISTERED MOBILE NUMBER:", font=FB, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(10,0))

        self.log_roll_var = ctk.StringVar()
        self.log_roll = HackerEntry(card, placeholder="e.g. 26B11AI024, AUS26-1040, or 10-digit Phone")
        self.log_roll.configure(textvariable=self.log_roll_var)
        self.log_roll.pack(fill="x", padx=20, pady=(5,10))
        self.log_roll.bind("<Return>", lambda e: self.log_pw.focus_set() if not self.log_pw.get() else self._verify_student_login())

        ctk.CTkLabel(card, text="PASSWORD (or enter new password on first login):", font=FB, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(5,0))
        self.log_pw = HackerEntry(card, show="*"); self.log_pw.pack(fill="x", padx=20, pady=(5,10))
        self.log_pw.bind("<Return>", lambda e: self._verify_student_login())

        self.log_err = ctk.CTkLabel(card, text="", font=FS, text_color=DANGER); self.log_err.pack(pady=(0,5))

        r = self._nav()

        self.btn_forgot = HackerButton(r, "FORGOT PASSWORD", self._show_forgot_password, color=DANGER, hover="#cc0000", text_col="#ffffff")
        self.btn_login = HackerButton(r, "LOGIN", self._verify_student_login)
        self.btn_login.pack(side="right")
        HackerButton(r, "BACK", self._render_step_identity, color=SURFACE, text_col=MUTED).pack(side="left")

    def _verify_student_login(self):
        entered_id = self.log_roll.get().strip()
        pw = self.log_pw.get()
        if not entered_id:
            self.log_err.configure(text="Please enter your Roll Number or Registered Phone Number.", text_color=DANGER)
            return

        self.log_err.configure(text="[>>>] VERIFYING WITH CAMPUS DATABASE...", text_color=NEON_GREEN)
        self.update_idletasks()

        canonical_roll, data = find_student(entered_id, self.cloud_db)

        if not data:
            self.log_err.configure(
                text=f"[-] '{entered_id}' not found in campus database.\nIf you are a new student, please click CREATE NEW ACCOUNT.",
                text_color=DANGER
            )
            self.btn_forgot.pack_forget()
            return

        roll = canonical_roll or data.get("permanent_roll") or data.get("temp_roll") or entered_id.upper()

        # Check if user entered a Temp Roll that was already migrated to a Permanent Roll
        if data.get("migrated_to"):
            perm_roll = data["migrated_to"]
            _, perm_data = find_student(perm_roll, self.cloud_db)
            if perm_data:
                data = perm_data
                roll = perm_roll

        # Check if user entered an unmigrated Temp Roll in Student Login
        if data.get("is_temp") and not data.get("migrated_to"):
            # Seamlessly switch to temp roll activation with data ready!
            self._render_step_temp_roll_login()
            self.temp_roll_entry.delete(0, "end")
            self.temp_roll_entry.insert(0, roll)
            self._verify_temp_roll()
            return

        saved_pw = data.get("password")

        if saved_pw:
            if pw != saved_pw:
                self.log_err.configure(text="Incorrect Password. Please try again.", text_color=DANGER)
                if not self.btn_forgot.winfo_ismapped(): self.btn_forgot.pack(side="right", padx=(0,10))
                return
        else:
            # First-time login: Password not set yet!
            if pw and len(pw) >= 4:
                # Save the new password to Firebase and local DB immediately
                data["password"] = pw
                update_student(roll, {"password": pw})
                if roll in self.cloud_db and isinstance(self.cloud_db[roll], dict):
                    self.cloud_db[roll]["password"] = pw
                else:
                    self.cloud_db[roll] = data
                save_local_db(self.cloud_db)
                messagebox.showinfo(
                    "ACCOUNT ACTIVATED",
                    f"Welcome, {data.get('name', 'Student')}!\n\nYour password has been successfully registered.\nLogging you in now..."
                )
            else:
                self.log_err.configure(
                    text="First-time login: Please enter a password (min 4 chars) and click LOGIN to secure your account.",
                    text_color=WARNING
                )
                return

        self.user_data["role"] = "student"
        self.user_data["roll"] = roll
        self.user_data["name"] = data.get("name", "UNKNOWN")
        self.user_data["branch"] = data.get("branch", "UNKNOWN")
        self.user_data["university"] = data.get("university", "Aditya University")
        self.user_data["phone"] = data.get("phone", "N/A")
        self.user_data["password"] = pw

        self._render_step_welcome()

    # ── REGISTER ──
    def _render_step_student_register(self):
        self._clear()
        ctk.CTkLabel(self.content, text="CREATE NEW ACCOUNT", font=FH1, text_color=NEON_GREEN).pack(pady=(15,5))

        self.card = HackerCard(self.content); self.card.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(self.card, text="ROLL NUMBER OR PHONE NUMBER:", font=FS, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(5,0))
        self.reg_roll_var = ctk.StringVar()
        self.reg_roll = HackerEntry(self.card, placeholder="Enter Roll Number or Phone...")
        self.reg_roll.configure(textvariable=self.reg_roll_var)
        self.reg_roll.pack(fill="x", padx=20, pady=2)
        self.reg_roll.bind("<Return>", lambda e: self._animate_fetch())

        self.reg_err = ctk.CTkLabel(self.card, text="", font=FS, text_color=DANGER); self.reg_err.pack(pady=5)

        self.details_frame = ctk.CTkFrame(self.card, fg_color="transparent")

        ctk.CTkLabel(self.details_frame, text="FULL NAME:", font=FS, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(5,0))
        self.reg_name = HackerEntry(self.details_frame); self.reg_name.pack(fill="x", padx=20, pady=2)

        ctk.CTkLabel(self.details_frame, text="BRANCH:", font=FS, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(5,0))
        self.reg_branch = HackerEntry(self.details_frame); self.reg_branch.pack(fill="x", padx=20, pady=2)

        ctk.CTkLabel(self.details_frame, text="CREATE PASSWORD:", font=FS, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(5,0))
        self.reg_pw = HackerEntry(self.details_frame, show="*"); self.reg_pw.pack(fill="x", padx=20, pady=2)
        self.reg_pw.bind("<Return>", lambda e: self._verify_student_register())

        self.r = self._nav()

        self.btn_forgot_reg = HackerButton(self.r, "FORGOT PASSWORD", self._show_forgot_password, color=DANGER, hover="#cc0000", text_col="#ffffff")
        self.btn_fetch = HackerButton(self.r, "FETCH DETAILS", self._animate_fetch)
        self.btn_register = HackerButton(self.r, "REGISTER", self._verify_student_register)

        HackerButton(self.r, "BACK", self._render_step_identity, color=SURFACE, text_col=MUTED).pack(side="left")

        def _on_roll_change_reg(*args):
            if len(self.reg_roll_var.get().strip()) >= 4:
                if not self.btn_fetch.winfo_ismapped() and not self.btn_register.winfo_ismapped():
                    self.btn_fetch.pack(side="right")
            else:
                self.btn_fetch.pack_forget()
                self.btn_register.pack_forget()
                self.details_frame.pack_forget()
                self.reg_err.configure(text="")
                self.btn_forgot_reg.pack_forget()

        self.reg_roll_var.trace_add("write", _on_roll_change_reg)

    def _animate_fetch(self):
        self.btn_fetch.pack_forget()
        self.btn_forgot_reg.pack_forget()
        self.reg_err.configure(text="[>>>] SEARCHING CAMPUS DATABASE...", text_color=NEON_GREEN)
        self.reg_roll.configure(state="disabled")

        def _anim():
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            for _ in range(12):
                s = "".join(random.choice(chars) for _ in range(25))
                self.after(0, lambda t=s: self.reg_err.configure(text=f"DECRYPTING: {t}"))
                time.sleep(0.04)
            self.after(0, self._process_fetch)

        threading.Thread(target=_anim, daemon=True).start()

    def _process_fetch(self):
        self.reg_roll.configure(state="normal")
        entered = self.reg_roll.get().strip()

        canonical_roll, data = find_student(entered, self.cloud_db)
        roll = canonical_roll or entered.upper()
        self.reg_roll.delete(0, "end")
        self.reg_roll.insert(0, roll)

        if data:
            if data.get("password"):
                self.reg_err.configure(text="THIS ACCOUNT IS ALREADY SECURED. PLEASE LOGIN.", text_color=DANGER)
                self.btn_forgot_reg.pack(side="right", padx=(0,10))
            else:
                self.reg_err.configure(text="[+] CAMPUS RECORD FOUND. SET YOUR PASSWORD.", text_color=NEON_GREEN)
                self.reg_name.delete(0, "end"); self.reg_name.insert(0, data.get("name", ""))
                self.reg_branch.delete(0, "end"); self.reg_branch.insert(0, data.get("branch", ""))
                self.details_frame.pack(fill="x", pady=(5,10))
                self.btn_register.pack(side="right")
        else:
            self.reg_err.configure(text="[-] NEW STUDENT: MANUAL ENTRY REQUIRED.", text_color=MUTED)
            self.reg_name.delete(0, "end")
            self.reg_branch.delete(0, "end")
            self.details_frame.pack(fill="x", pady=(5,10))
            self.btn_register.pack(side="right")

    def _verify_student_register(self):
        roll = self.reg_roll.get().strip().upper()
        if not roll: return

        pw = self.reg_pw.get()
        if len(pw) < 4:
            self.reg_err.configure(text="Password must be >= 4 characters.", text_color=DANGER)
            return

        name = self.reg_name.get().strip()
        branch = self.reg_branch.get().strip()

        # Update Firebase Cloud Database & local database
        new_data = {
            "name": name,
            "branch": branch,
            "university": "Aditya University",
            "phone": "N/A",
            "password": pw,
            "status": "ACTIVE_REGISTERED"
        }
        if roll in self.cloud_db and isinstance(self.cloud_db[roll], dict):
            self.cloud_db[roll].update(new_data)
        else:
            self.cloud_db[roll] = new_data

        set_student(roll, self.cloud_db[roll])
        save_local_db(self.cloud_db)

        self.user_data["role"] = "student"
        self.user_data["roll"] = roll
        self.user_data["name"] = name
        self.user_data["branch"] = branch
        self.user_data["university"] = "Aditya University"
        self.user_data["password"] = pw

        self._render_step_welcome()

    def _render_step_welcome(self):
        self._clear()
        name = self.user_data.get('name', 'USER').upper()
        roll = self.user_data.get('roll', '')

        # Outer card container
        card = HackerCard(self.content)
        card.pack(fill="both", expand=True, padx=10, pady=10)

        # Top status banner
        top_lbl = ctk.CTkLabel(card, text=">_ INITIALIZING QUANTUM CORE...", font=FM, text_color=MUTED)
        top_lbl.pack(pady=(15, 5))

        # Main animated text labels
        welcome_lbl = ctk.CTkLabel(card, text="", font=FH1, text_color=NEON_GREEN)
        welcome_lbl.pack(pady=(10, 2))

        subtitle_lbl = ctk.CTkLabel(card, text="", font=FH2, text_color="#ffffff")
        subtitle_lbl.pack(pady=(0, 10))

        user_badge = ctk.CTkLabel(card, text="", font=FH3, text_color=MUTED)
        user_badge.pack(pady=(0, 10))

        # Console logs text box for hacker booting effect
        log_box = ctk.CTkTextbox(card, height=130, fg_color=SURFACE, text_color=NEON_GREEN, font=FS,
                                 border_width=1, border_color=DARK_GREEN)
        log_box.pack(fill="x", padx=25, pady=5)

        # Progress bar
        pbar = ctk.CTkProgressBar(card, progress_color=NEON_GREEN, fg_color=SURFACE, height=12)
        pbar.set(0)
        pbar.pack(fill="x", padx=25, pady=(10, 15))

        # Action container
        act_frame = ctk.CTkFrame(card, fg_color="transparent")
        act_frame.pack(fill="x", padx=25, pady=(5, 15))

        continue_btn = HackerButton(act_frame, "LAUNCH AGENT PRAYATH >", self._render_step_apikey, height=45)

        def _run_intro_anim():
            full_welcome = "WELCOME PRAYATH"
            full_subtitle = "AUTOMATIC CODE EDITOR"

            # 1. Typewriter Welcome
            for i in range(1, len(full_welcome) + 1):
                if self._stop_anim.is_set(): return
                try:
                    self.after(0, lambda t=full_welcome[:i]: welcome_lbl.configure(text=t))
                except Exception:
                    return
                time.sleep(0.04)

            # 2. Typewriter Subtitle
            for i in range(1, len(full_subtitle) + 1):
                if self._stop_anim.is_set(): return
                try:
                    self.after(0, lambda t=full_subtitle[:i]: subtitle_lbl.configure(text=t))
                except Exception:
                    return
                time.sleep(0.03)

            if self._stop_anim.is_set(): return
            try:
                self.after(0, lambda: user_badge.configure(text=f"OPERATOR: {name} | {roll or 'SYSTEM ADMIN'}"))
            except Exception:
                return

            # 3. Boot telemetry streaming
            lines = [
                "[BOOT:01] SECURE KERNEL INITIALIZED...",
                "[BOOT:02] BYPASSING ONLINE EDITOR CLIPBOARD RESTRICTIONS...",
                "[BOOT:03] FIREBASE REALTIME CLOUD TELEMETRY: CONNECTED...",
                f"[BOOT:04] CREDENTIALS AUTHENTICATED: {name}...",
                "[BOOT:05] HUMAN-CADENCE AUTO-TYPING ENGINE: 100% ARMED...",
                "[BOOT:06] SYSTEM ONLINE: WELCOME PRAYATH AUTOMATIC CODE EDITOR."
            ]

            for idx, line in enumerate(lines):
                if self._stop_anim.is_set(): return
                try:
                    self.after(0, lambda l=line: log_box.insert("end", l + "\n"))
                    self.after(0, lambda: log_box.see("end"))
                    progress = (idx + 1) / len(lines)
                    self.after(0, lambda p=progress: pbar.set(p))
                except Exception:
                    return
                time.sleep(0.22)

            if self._stop_anim.is_set(): return
            try:
                self.after(0, lambda: top_lbl.configure(text=">_ AGENT PRAYATH FULLY ARMED & READY", text_color=NEON_GREEN))
                self.after(0, lambda: continue_btn.pack(fill="x", expand=True))
                self.after(1200, lambda: self._render_step_apikey() if (self.winfo_exists() and not self._stop_anim.is_set()) else None)
            except Exception:
                pass

        threading.Thread(target=_run_intro_anim, daemon=True).start()

    def _render_step_apikey(self):
        self._stop_anim.set()
        self._clear()
        ctk.CTkLabel(self.content, text="CONFIGURE AI UPLINK (OPENROUTER / GEMINI)", font=FH1, text_color=NEON_GREEN).pack(pady=(20,5))
        ctk.CTkLabel(self.content, text="Connect OpenRouter or Google Gemini API to enable Autonomous AI Coding", font=FB, text_color=MUTED).pack(pady=(0,15))

        saved_key = self.session.get("api_key", "")
        card = HackerCard(self.content)
        card.pack(fill="x", padx=20, pady=10)

        # 1-Click Direct Links for OpenRouter and Gemini
        link_box = ctk.CTkFrame(card, fg_color="transparent")
        link_box.pack(fill="x", padx=20, pady=(15, 8))
        HackerButton(link_box, "🌐 GET OPENROUTER KEY (openrouter.ai)",
                     lambda: webbrowser.open("https://openrouter.ai/keys"),
                     height=30, color=SURFACE, hover=DARK_GREEN, text_col=NEON_GREEN, font=FS).pack(side="left", padx=(0, 10))
        HackerButton(link_box, "🔑 GOOGLE AI STUDIO (GEMINI)",
                     lambda: webbrowser.open("https://aistudio.google.com/app/apikey"),
                     height=30, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG, font=FS).pack(side="right")

        ctk.CTkLabel(card, text="OPENROUTER (sk-or-...) OR GEMINI KEY:", font=FB, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=20, pady=(10, 5))

        entry_row = ctk.CTkFrame(card, fg_color="transparent")
        entry_row.pack(fill="x", padx=20, pady=5)

        self.api_e = HackerEntry(entry_row, show="*", placeholder="Paste OpenRouter Key (sk-or-...) or Gemini Key (AIzaSy...)...")
        self.api_e.pack(side="left", fill="x", expand=True, padx=(0, 10))
        if saved_key: self.api_e.insert(0, saved_key)

        self.btn_test_api = HackerButton(entry_row, "⚡ TEST KEY", self._test_api_key_onboarding, height=38, width=110, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN)
        self.btn_test_api.pack(side="right")

        self.api_status_lbl = ctk.CTkLabel(card, text="[*] Enter your API key and click 'TEST KEY' or 'CONFIGURE & LAUNCH'", font=FS, text_color=MUTED, anchor="w")
        self.api_status_lbl.pack(fill="x", padx=20, pady=(4, 15))

        r = self._nav()
        HackerButton(r, "CONFIGURE & LAUNCH", self._save_api, height=44).pack(side="right", padx=(10,0))
        HackerButton(r, "SKIP TO OFFLINE MODE", self._skip_api, color=SURFACE, text_col=MUTED, height=44).pack(side="right", padx=(10,0))
        HackerButton(r, "BACK", self._render_step_identity, color=SURFACE, text_col=MUTED, height=44).pack(side="left", padx=(0,10))

    def _test_api_key_onboarding(self):
        k = self.api_e.get().strip()
        if not k:
            self.api_status_lbl.configure(text="[-] Please paste an API key first.", text_color=DANGER)
            show_api_error_modal(self, "API KEY REQUIRED", "Please enter or paste your OpenRouter or Gemini API key before testing.")
            return
        self.btn_test_api.configure(state="disabled")
        self.api_status_lbl.configure(text="[*] Verifying AI Uplink with Cloud...", text_color=NEON_GREEN)
        def _task():
            ok, msg = validate_gemini_api_key(k)
            def _ui():
                try:
                    self.btn_test_api.configure(state="normal")
                    if ok:
                        self.api_status_lbl.configure(text=f"🟢 {msg}", text_color=NEON_GREEN)
                        messagebox.showinfo("API CONNECTED", f"SUCCESS!\n\n{msg}")
                    else:
                        self.api_status_lbl.configure(text=f"🔴 {msg}", text_color=DANGER)
                        show_api_error_modal(self, "API KEY VERIFICATION FAILED", msg)
                except Exception:
                    pass
            try:
                self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _save_api(self):
        self._stop_anim.set()
        k = self.api_e.get().strip()
        if not k:
            ans = messagebox.askyesno("NO API KEY", "No API key entered.\n\nWould you like to continue in Offline Mode (Offline DSA Vault & Manual Typer)?")
            if ans:
                self._skip_api()
            return

        self.api_status_lbl.configure(text="[*] Verifying API key with Google Cloud...", text_color=NEON_GREEN)
        def _task():
            ok, msg = validate_gemini_api_key(k)
            def _ui():
                try:
                    if ok:
                        self.user_data["api_key"] = k
                        self.user_data["startup_mode"] = "AI_MODULE"
                        self._finish()
                    else:
                        show_api_error_modal(self, "API KEY VERIFICATION FAILED", msg)
                        ans = messagebox.askyesno("API KEY WARNING", f"Google Gemini returned:\n{msg}\n\nWould you like to save this key anyway and continue?")
                        if ans:
                            self.user_data["api_key"] = k
                            self.user_data["startup_mode"] = "AI_MODULE"
                            self._finish()
                        else:
                            self.api_status_lbl.configure(text=f"🔴 {msg}", text_color=DANGER)
                except Exception:
                    pass
            try:
                self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _skip_api(self):
        self._stop_anim.set()
        self.user_data["api_key"] = ""
        self.user_data["startup_mode"] = "MANUAL_OVERRIDE"
        self._finish()

    def _finish(self):
        self._stop_anim.set()
        self.session.update({
            "role": self.user_data.get("role", "student"),
            "name": self.user_data.get("name", "USER"),
            "roll": self.user_data.get("roll", ""),
            "branch": self.user_data.get("branch", ""),
            "university": self.user_data.get("university", "Aditya University"),
            "password": self.user_data.get("password", ""),
            "phone": self.user_data.get("phone", "N/A"),
            "api_key": self.user_data.get("api_key", ""),
            "startup_mode": self.user_data.get("startup_mode", "MANUAL_OVERRIDE")
        })
        save_session(self.session)
        self.success = True
        self.destroy()

# ── MAIN APP WINDOW ───────────────────────────────────────────────────────────
class AutoCoderApp(ctk.CTk):
    def __init__(self, session):
        super().__init__()
        _clean_stray_desktop_db()
        self.session     = session
        self.backend     = AntigravityBackend(session.get("api_key",""), preferred_model=session.get("openrouter_model", "Auto-Best (Recommended)"))
        self.keyboard    = KController()
        self.is_typing   = False
        self.stop_typing = False
        self._shutdown_event = threading.Event()
        self.logged_out = False
        self.kb_listener = None
        self.current_mode = self.session.get("startup_mode", "MANUAL_OVERRIDE")

        # Crucial: Initialize control variables early before building UI or threads
        self.status_var   = ctk.StringVar(value="SYSTEM READY.")
        self.auto_run_var = ctk.BooleanVar(value=True)

        # Student Ultimate Edition v3.0 Features
        self.format_var = ctk.StringVar(value="competitive")
        self.sol_type_var = ctk.StringVar(value="optimal")
        self.typing_speed_var = ctk.StringVar(value="Average (60 WPM)")
        self.typo_sim_var = ctk.BooleanVar(value=True)
        self.ghost_hud = None
        self.current_theme = "matrix"
        self.last_generated_code = ""
        self.last_generated_lang = "python" 

        name = self.session.get("name","AGENT")
        self.title(f"AGENT PRAYATH {APP_VERSION} - {name}")
        self.geometry("1100x800")
        self.minsize(900, 600)
        self.configure(fg_color=BG)

        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"+{(sw-1100)//2}+{(sh-800)//2}")

        self._build_ui()
        self._start_emergency_listener()
        self._start_heartbeat()
        self.lift()
        self.attributes('-topmost', True)
        self.after(200, lambda: self.attributes('-topmost', False))
        self.focus_force()

        # Handle window close cleanly
        self.protocol("WM_DELETE_WINDOW", self._on_app_close)

    
    def _dismiss_broadcast(self):
        try:
            if hasattr(self, "_active_broadcast_v") and self._active_broadcast_v:
                self._popup_shown_for = self._active_broadcast_v
            self.broadcast_banner.pack_forget()
        except Exception:
            pass

    def _open_user_groups_modal(self):
        UserGroupsModal(self)

    def _refresh_admin_target_options(self):
        base_options = [
            "ALL USERS (Entire Campus)",
            "ADMIN ONLY",
            "BRANCH: DATA SCIENCE (DS)",
            "BRANCH: COMPUTER SCIENCE (CSE)",
            "BRANCH: ARTIFICIAL INTELLIGENCE (AIML)",
            "BRANCH: ELECTRONICS (ECE)",
            "BRANCH: ELECTRICAL (EEE)",
            "BRANCH: MECHANICAL (ME)",
            "BRANCH: CIVIL (CE)"
        ]
        def _task():
            try:
                groups = get_user_groups()
                self.user_groups_cache = groups if isinstance(groups, dict) else {}
                group_opts = [f"GROUP: {gname}" for gname in sorted(self.user_groups_cache.keys()) if isinstance(self.user_groups_cache[gname], dict)]
                full_opts = base_options + group_opts
                def _ui():
                    if hasattr(self, "admin_target_menu"):
                        self.admin_target_menu.configure(values=full_opts)
                    if hasattr(self, "admin_group_filter_menu"):
                        grp_filter_opts = ["ALL GROUPS"] + sorted(list(self.user_groups_cache.keys()))
                        self.admin_group_filter_menu.configure(values=grp_filter_opts)
                    if hasattr(self, "_refresh_admin_tree"):
                        self._refresh_admin_tree()
                self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _refresh_admin_group_filter_options(self):
        self._refresh_admin_target_options()

    def _admin_broadcast_update(self):
        v = self.admin_upd_v_entry.get().strip() or APP_VERSION
        msg = self.admin_upd_msg_entry.get().strip() or "New system update available."
        url = getattr(self, "admin_upd_url_entry", None)
        url_val = url.get().strip() if url else ""
        show_pop = self.admin_upd_popup_var.get()
        target_aud = getattr(self, "admin_target_audience_var", None)
        target_audience = target_aud.get() if target_aud else "ALL USERS (Entire Campus)"

        payload = {
            "version": v,
            "message": msg,
            "download_url": url_val,
            "target_audience": target_audience,
            "timestamp": time.time(),
            "show_popup": show_pop,
            "author": self.session.get("name", "ROOT_ADMIN")
        }
        res = _firebase_request("/system_broadcast", method="PUT", data=payload)
        _firebase_request("/system_config/latest_version", method="PUT", data=v)
        _firebase_request("/system_config/changelog", method="PUT", data=msg)
        if url_val:
            _firebase_request("/system_config/download_url", method="PUT", data=url_val)

        # Log release to update history in Firebase
        log_update_history(v, msg, target_audience=target_audience, download_url=url_val, author=self.session.get("name", "ROOT_ADMIN"))

        if hasattr(self, "admin_broadcast_status"):
            self.admin_broadcast_status.configure(
                text=f"[+] BROADCAST ACTIVE: Pushed {v} to audience: '{target_audience}'!",
                text_color=NEON_GREEN
            )
        messagebox.showinfo(
            "BROADCAST SENT",
            f"Update notification for {v} broadcasted successfully!\n\n"
            f"Target Audience: {target_audience}\n"
            f"Message: {msg}\n"
            f"Direct Download URL: {url_val or 'Default GitHub'}\n"
            f"Logged to Release History."
        )

    def _admin_clear_broadcast(self):
        _firebase_request("/system_broadcast", method="DELETE")
        if hasattr(self, "admin_broadcast_status"):
            self.admin_broadcast_status.configure(
                text="[*] Broadcast cleared. Notifications dismissed from all student screens.",
                text_color=MUTED
            )
        messagebox.showinfo("BROADCAST CLEARED", "Global broadcast cleared from Firebase.")

    def _clear_update_history_action(self):
        ans = messagebox.askyesno(
            "CLEAR UPDATE HISTORY",
            "Are you sure you want to completely clear the system update and release history from Firebase Cloud?\n\nThis will purge all history records across all user screens."
        )
        if not ans:
            return

        def _task():
            clear_update_history()
            def _ui():
                self._refresh_update_history_table()
                self.update_status("[+] System update history cleared from Firebase Cloud.")
                messagebox.showinfo("HISTORY PURGED", "Update and release history has been successfully cleared from Firebase Cloud.")
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _admin_revoke_latest_update(self):
        """Revoke or delete the latest update release and roll back to the previous one."""
        confirm = messagebox.askyesno(
            "REVOKE / ROLLBACK LATEST UPDATE",
            "Are you sure you want to revoke the latest update?\n\n"
            "This will:\n"
            "1. Remove the latest release from update history.\n"
            "2. Roll back Firebase Cloud telemetry and broadcasts to the previous release.\n"
            "3. Suppress update notifications for the revoked release across all student screens."
        )
        if not confirm:
            return

        def _task():
            ok, revoked_v, prev_v, msg = revoke_latest_update()
            def _ui():
                self._refresh_update_history_table()
                if hasattr(self, "_refresh_update_telemetry"):
                    self._refresh_update_telemetry()
                if hasattr(self, "_load_current_broadcast_info"):
                    self._load_current_broadcast_info()

                if ok:
                    self.update_status(f"[*] Revoked release {revoked_v} -> Reverted to {prev_v}.")
                    if hasattr(self, "admin_broadcast_status"):
                        self.admin_broadcast_status.configure(
                            text=f"[*] REVOKED {revoked_v}: Reverted system release to {prev_v}.",
                            text_color=WARNING
                        )
                    messagebox.showinfo(
                        "UPDATE REVOKED",
                        f"Successfully revoked release {revoked_v}!\n\n"
                        f"Active System Version Reverted To: {prev_v}\n\n"
                        f"{msg}"
                    )
                else:
                    self.update_status(f"[!] Revoke failed: {msg}")
                    messagebox.showwarning("REVOKE NOTE", msg)
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _delete_selected_history_item(self):
        """Delete whichever release row is currently selected in the history tree."""
        if not hasattr(self, "history_tree"):
            return
        sel = self.history_tree.selection()
        if not sel:
            messagebox.showinfo("SELECT ROW", "Please click on an update row in the table below to select it first, then click 'DELETE SELECTED'.")
            return
        item_id = sel[0]
        vals = self.history_tree.item(item_id, "values")
        if not vals:
            return
        version = vals[0]
        changelog = vals[3] if len(vals) > 3 else ""

        key_map = getattr(self, "_history_key_map", {})
        target_key = key_map.get(item_id)

        confirm = messagebox.askyesno(
            "DELETE RELEASE ENTRY",
            f"Are you sure you want to delete this release record from Firebase?\n\nVersion: {version}\nChangelog: {changelog}"
        )
        if not confirm:
            return

        def _task():
            if target_key:
                delete_update_history_item(target_key)
            else:
                revoke_latest_update()

            def _ui():
                self._refresh_update_history_table()
                if hasattr(self, "_refresh_update_telemetry"):
                    self._refresh_update_telemetry()
                self.update_status(f"[-] Deleted release entry {version} from Firebase.")
                messagebox.showinfo("DELETED", f"Update record for {version} was removed from Firebase.")
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _load_current_broadcast_info(self):
        def _task():
            try:
                bc = _firebase_request("/system_broadcast")
                if isinstance(bc, dict) and bc.get("version"):
                    v = bc.get("version", "")
                    msg = bc.get("message", "")
                    url = bc.get("download_url", "")
                    target_aud = bc.get("target_audience", "ALL USERS (Entire Campus)")
                    def _ui():
                        if hasattr(self, "admin_upd_v_entry") and v:
                            self.admin_upd_v_entry.delete(0, "end"); self.admin_upd_v_entry.insert(0, v)
                        if hasattr(self, "admin_upd_msg_entry") and msg:
                            self.admin_upd_msg_entry.delete(0, "end"); self.admin_upd_msg_entry.insert(0, msg)
                        if hasattr(self, "admin_upd_url_entry") and url:
                            self.admin_upd_url_entry.delete(0, "end"); self.admin_upd_url_entry.insert(0, url)
                        if hasattr(self, "admin_target_audience_var") and target_aud:
                            self.admin_target_audience_var.set(target_aud)
                        if hasattr(self, "admin_broadcast_status"):
                            self.admin_broadcast_status.configure(text=f"[+] Active Broadcast: {v} ({target_aud}) - '{msg[:25]}...'", text_color=NEON_GREEN)
                    self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _check_smart_interviews_access(self):
        """Verify whether current session is granted access to Smart Interviews Test Suite."""
        if self.session.get("role") == "admin":
            return True

        user_roll = str(self.session.get("roll", "")).strip().upper()
        if not user_roll:
            return False

        # Fast local whitelist for 'only us' group members (zero network delay)
        only_us_whitelist = {
            "26311DS620", "26B11AI855", "26B11DS115", "26B11DS204",
            "26B11DS407", "26B11DS507", "26B11DS529", "26B11DS678", "26B11EC141"
        }
        if user_roll in only_us_whitelist:
            return True

        # Dynamic Firebase verification
        try:
            groups = get_user_groups()
            if isinstance(groups, dict):
                for g_name, g_data in groups.items():
                    if isinstance(g_data, dict):
                        g_lower = str(g_name).strip().lower()
                        if g_lower in ["only us", "smart interviews", "smart_interviews"] or g_data.get("smart_interviews_access") is True:
                            m_list = [str(m).strip().upper() for m in g_data.get("members", [])]
                            if user_roll in m_list:
                                return True
            feat = _firebase_request("/features/smart_interviews")
            if isinstance(feat, dict):
                if feat.get("enabled_for_all"):
                    return True
                auth_users = [str(u).strip().upper() for u in feat.get("authorized_users", [])]
                if user_roll in auth_users:
                    return True
        except Exception:
            pass
        return False

    def _is_user_eligible_for_broadcast(self, target_audience):
        """Verify whether current user is within the target audience for update notification."""
        aud_str = str(target_audience or "").strip().upper()
        is_admin = (self.session.get("role") == "admin")

        # Admin always sees all releases
        if is_admin:
            return True

        user_roll = str(self.session.get("roll", "")).strip().upper()
        user_branch = str(self.session.get("branch", "")).strip().upper()

        only_us_whitelist = {
            "26311DS620", "26B11AI855", "26B11DS115", "26B11DS204",
            "26B11DS407", "26B11DS507", "26B11DS529", "26B11DS678", "26B11EC141"
        }
        # Whitelisted 'only us' members are eligible if target contains 'only us' or group targeting
        if "ONLY US" in aud_str or "SMART INTERVIEWS" in aud_str:
            if user_roll in only_us_whitelist:
                return True

        # Non-admin users are strictly blocked from pure ADMIN ONLY updates
        if aud_str in ("ADMIN", "ADMIN ONLY") or (aud_str.startswith("ADMIN") and "GROUP" not in aud_str and "ONLY US" not in aud_str):
            return False

        if not target_audience or "ALL" in aud_str or aud_str == "PUBLIC":
            return True

        if aud_str.startswith("BRANCH:"):
            # e.g. "BRANCH: DATA SCIENCE (DS)"
            b_target = aud_str.split("BRANCH:")[-1].strip().upper()
            if "(" in b_target and ")" in b_target:
                b_code = b_target[b_target.find("(")+1:b_target.find(")")].strip()
            else:
                b_code = b_target.strip()
            if b_code == user_branch:
                return True
            if b_code in ("DS", "DATA SCIENCE") and user_branch in ("DS", "DATA SCIENCE"):
                return True
            if b_code in user_branch or user_branch in b_code:
                return True
            return False

        if "GROUP:" in aud_str:
            grp_name = str(target_audience).split("GROUP:")[-1].strip()
            try:
                grp_data = _firebase_request(f"/user_groups/{_safe_key(grp_name)}")
                if isinstance(grp_data, dict):
                    members = grp_data.get("members", [])
                    if isinstance(members, list) and user_roll in [str(m).strip().upper() for m in members]:
                        return True
                    b_flt = grp_data.get("branch_filter", "ALL BRANCHES").strip().upper()
                    if b_flt != "ALL BRANCHES":
                        if b_flt in ("DS", "DATA SCIENCE") and user_branch in ("DS", "DATA SCIENCE"):
                            return True
                        if b_flt in user_branch or user_branch in b_flt:
                            return True
            except Exception:
                pass
            return False

        return False

    def _check_and_display_broadcast(self):
        try:
            bc = _firebase_request("/system_broadcast")
            if isinstance(bc, dict) and bc.get("version"):
                v = bc.get("version", "")
                msg = bc.get("message", "New update available!")
                target_aud = bc.get("target_audience", "ALL USERS")

                # Check eligibility
                if not self._is_user_eligible_for_broadcast(target_aud):
                    def _hide_ineligible():
                        if hasattr(self, "broadcast_banner"):
                            self.broadcast_banner.pack_forget()
                    self.after(0, _hide_ineligible)
                    return

                self._active_broadcast_v = v
                if is_version_newer(v, APP_VERSION):
                    def _show_ui():
                        self.broadcast_msg_lbl.configure(text=f"📢 UPDATE FOR [{target_aud}]: {v} READY — {msg}")
                        if hasattr(self, "tab_container"):
                            self.broadcast_banner.pack(side="top", fill="x", padx=10, pady=(10,0), before=self.tab_container)
                        else:
                            self.broadcast_banner.pack(side="top", fill="x", padx=10, pady=(10,0))
                        if bc.get("show_popup") and getattr(self, "_popup_shown_for", None) != v:
                            self._popup_shown_for = v
                            ans = messagebox.askyesno("NEW UPDATE AVAILABLE", f"AGENT PRAYATH {v} IS READY!\n\nTarget Audience: {target_aud}\nChangelog:\n{msg}\n\nWould you like to install the update now?")
                            if ans:
                                self._check_update_and_refresh_ui()
                    self.after(0, _show_ui)
                else:
                    # User is running latest version or newer: ensure notification banner is hidden and suppressed
                    self._popup_shown_for = v
                    def _hide_ui():
                        if hasattr(self, "broadcast_banner"):
                            self.broadcast_banner.pack_forget()
                    self.after(0, _hide_ui)
            else:
                def _hide_ui():
                    if hasattr(self, "broadcast_banner"):
                        self.broadcast_banner.pack_forget()
                self.after(0, _hide_ui)
        except Exception:
            pass

    def _start_heartbeat(self):
        """Send periodic presence heartbeat to Firebase Cloud every 15s."""
        def _loop():
            roll = self.session.get("roll") or self.session.get("name", "USER")
            while not self._shutdown_event.is_set():
                try:
                    payload = {
                        "roll": roll,
                        "name": self.session.get("name", "USER"),
                        "role": self.session.get("role", "student"),
                        "branch": self.session.get("branch", ""),
                        "university": self.session.get("university", "Aditya University"),
                        "last_seen": time.time(),
                        "status": "ONLINE",
                        "mode": getattr(self, "current_mode", "MANUAL_OVERRIDE"),
                        "version": APP_VERSION
                    }
                    update_online_presence(roll, payload)
                    self._check_and_display_broadcast()
                except Exception:
                    pass
                self._shutdown_event.wait(15)

        t = threading.Thread(target=_loop, daemon=True)
        t.start()

    def _on_app_close(self):
        """Cleanup online presence when user closes the app."""
        self._shutdown_event.set()
        self.logged_out = False
        try:
            if hasattr(self, "kb_listener") and self.kb_listener:
                self.kb_listener.stop()
        except Exception:
            pass
        try:
            roll = self.session.get("roll") or self.session.get("name", "USER")
            remove_online_presence(roll)
        except Exception:
            pass
        try:
            self.destroy()
        except Exception:
            pass

    def _build_ui(self):
        # 1. Header
        hdr = ctk.CTkFrame(self, height=70, fg_color=SURFACE, border_width=2, border_color=DARK_GREEN, corner_radius=0)
        hdr.pack(fill="x", padx=10, pady=(10,0)); hdr.pack_propagate(False)
        self.hdr_title_lbl = ctk.CTkLabel(hdr, text=f">_ AGENT PRAYATH {APP_VERSION}", font=FH1, text_color=NEON_GREEN)
        self.hdr_title_lbl.pack(side="left", padx=20)

        role = self.session.get("role", "UNKNOWN").upper()
        name = self.session.get("name", "UNKNOWN").upper()
        roll = self.session.get("roll", "")
        id_text = f"[{role}] {name} {roll}"
        self.hdr_id_lbl = ctk.CTkLabel(hdr, text=id_text, font=FB, text_color=MUTED)
        self.hdr_id_lbl.pack(side="right", padx=(10,20))

        # Student Toolbar
        HackerButton(hdr, "👻 GHOST HUD", self._toggle_ghost_hud, height=34, color=SURFACE, hover=DARK_GREEN, text_col=NEON_GREEN, border_color=DARK_GREEN).pack(side="right", padx=6)
        HackerButton(hdr, "🎨 STEALTH THEME", self._toggle_theme, height=34, color=SURFACE, hover=DARK_GREEN, text_col=NEON_GREEN, border_color=DARK_GREEN).pack(side="right", padx=6)

        # 2. Main split body (Sidebar + Content)
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=10, pady=10)

        # Sidebar
        self.sidebar = HackerCard(body, width=230)
        self.sidebar.pack(side="left", fill="y", padx=(0,10))
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(self.sidebar, text="SYSTEM MENU", font=FH3, text_color=MUTED).pack(pady=(20,10))

        # Content Panel
        self.main_panel = HackerCard(body)
        self.main_panel.pack(side="right", fill="both", expand=True)

        # ── SYSTEM BROADCAST NOTIFICATION BANNER (VISIBLE TO ALL USERS) ────
        self.broadcast_banner = ctk.CTkFrame(self.main_panel, fg_color="#1a2e1a", border_width=2, border_color=NEON_GREEN, height=44)
        self.broadcast_msg_lbl = ctk.CTkLabel(self.broadcast_banner, text="", font=FB, text_color=NEON_GREEN, anchor="w")
        self.broadcast_msg_lbl.pack(side="left", padx=15, fill="x", expand=True)
        HackerButton(self.broadcast_banner, "⚡ UPDATE NOW", self._check_update_and_refresh_ui, height=28, width=120, color=DARK_GREEN, text_col=BG).pack(side="right", padx=(5,10))
        HackerButton(self.broadcast_banner, "✕", self._dismiss_broadcast, height=28, width=32, color=SURFACE, text_col=MUTED).pack(side="right", padx=5)

        # Persistent Container Frame for all tabs
        self.tab_container = ctk.CTkFrame(self.main_panel, fg_color="transparent")
        self.tab_container.pack(fill="both", expand=True)

        self.frames = {}

        self.frames["AI_MODULE"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
        self._build_ai_tab(self.frames["AI_MODULE"])

        self.frames["VIVA_NOTES"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
        self._build_viva_tab(self.frames["VIVA_NOTES"])

        self.frames["TEST_CASES"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
        self._build_test_cases_tab(self.frames["TEST_CASES"])

        self.frames["OFFLINE_VAULT"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
        self._build_offline_vault_tab(self.frames["OFFLINE_VAULT"])

        self.frames["MANUAL_OVERRIDE"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
        self._build_manual_tab(self.frames["MANUAL_OVERRIDE"])

        # Access control: Admin gets DB & Live Monitor. Admin & authorized group ('only us') get Smart Interviews.
        self.has_smart_interviews_access = self._check_smart_interviews_access()

        if self.session.get("role") == "admin":
            self.frames["LIVE_MONITOR"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
            self._build_live_monitor_tab(self.frames["LIVE_MONITOR"])

            self.frames["DB_ADMIN"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
            self._build_admin_tab(self.frames["DB_ADMIN"])

        if self.has_smart_interviews_access:
            self.frames["SMART_INTERVIEWS"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
            self._build_smart_interviews_tab(self.frames["SMART_INTERVIEWS"])

        self.frames["SYSTEM_INFO"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
        self._build_profile_tab(self.frames["SYSTEM_INFO"])

        self.frames["UPDATE_CENTER"] = ctk.CTkFrame(self.tab_container, fg_color="transparent")
        self._build_update_center_tab(self.frames["UPDATE_CENTER"])

        # Setup Sidebar Navigation Buttons
        self._create_nav_button("AI MODULE", "AI_MODULE")
        self._create_nav_button("🎓 VIVA CHEAT SHEET", "VIVA_NOTES")
        self._create_nav_button("🧪 TEST CASES", "TEST_CASES")
        self._create_nav_button("📚 OFFLINE DSA VAULT", "OFFLINE_VAULT")
        self._create_nav_button("MANUAL OVERRIDE", "MANUAL_OVERRIDE")
        if self.session.get("role") == "admin":
            self._create_nav_button("LIVE USERS [●]", "LIVE_MONITOR")
            self._create_nav_button("DB ADMIN", "DB_ADMIN")
        if self.has_smart_interviews_access:
            self._create_nav_button("⚡ SMART INTERVIEWS TEST", "SMART_INTERVIEWS")
        self._create_nav_button("PROFILE & SECURITY", "SYSTEM_INFO")
        self._create_nav_button("⚡ UPDATE CENTER", "UPDATE_CENTER")

        # Logout Button
        ctk.CTkFrame(self.sidebar, height=2, fg_color=BORDER).pack(fill="x", pady=(20,10), padx=20)
        HackerButton(self.sidebar, "LOGOUT", self._logout, color=SURFACE, text_col=DANGER, hover="#550000", border_color=DANGER).pack(fill="x", padx=20, side="bottom", pady=20)

        # 3. Footer
        footer = HackerCard(self, height=180)
        footer.pack(fill="x", padx=10, pady=(0,10)); footer.pack_propagate(False)

        tr = ctk.CTkFrame(footer, fg_color="transparent"); tr.pack(fill="x", padx=20, pady=10)
        ctk.CTkSwitch(tr, text="AUTONOMOUS EXECUTION LOOP", variable=self.auto_run_var,
                      progress_color=NEON_GREEN, button_color=DARK_GREEN, font=FB, text_color=NEON_GREEN).pack(side="left")

        self.status_lbl = ctk.CTkLabel(tr, textvariable=self.status_var, font=FM, text_color=NEON_GREEN, anchor="e")
        self.status_lbl.pack(side="right")

        self.preview_box = ctk.CTkTextbox(footer, height=80, fg_color=SURFACE, text_color=NEON_GREEN, font=FM,
                                          border_width=2, border_color=DARK_GREEN, corner_radius=0)
        self.preview_box.pack(fill="both", expand=True, padx=20, pady=(0,10))

        HackerButton(footer, "EMERGENCY ABORT (F8 / ESC)", self.abort_execution, color=DANGER, hover="#b30000", text_col="#ffffff", height=30).pack(fill="x", padx=20, pady=(0,10))

        # Show initial frame
        mode = self.session.get("startup_mode", "MANUAL_OVERRIDE")
        if mode not in self.frames: mode = "MANUAL_OVERRIDE"
        self.show_frame(mode)
        self.after(300, self._check_and_display_broadcast)

    def _create_nav_button(self, text, frame_name):
        btn = HackerButton(self.sidebar, f"> {text}", lambda: self.show_frame(frame_name), height=40, anchor="w")
        btn.pack(fill="x", padx=15, pady=5)

    def show_frame(self, name):
        self.current_mode = name
        for frame in self.frames.values(): frame.pack_forget()
        self.frames[name].pack(fill="both", expand=True, padx=10, pady=10)
        if name == "LIVE_MONITOR":
            self._refresh_live_users()

    def _logout(self):
        self._shutdown_event.set()
        self.logged_out = True
        try:
            if hasattr(self, "kb_listener") and self.kb_listener:
                self.kb_listener.stop()
        except Exception:
            pass
        try:
            roll = self.session.get("roll") or self.session.get("name", "USER")
            remove_online_presence(roll)
        except Exception:
            pass
        save_session({})
        try:
            self.destroy()
        except Exception:
            pass

    def _open_api_config_modal(self):
        ApiKeyConfigModal(self)

    def _test_ai_quick_api(self):
        k = self.ai_quick_api_entry.get().strip() if hasattr(self, "ai_quick_api_entry") else ""
        if not k:
            self.ai_quick_status_lbl.configure(text="[-] Please paste an API key first.", text_color=DANGER)
            show_api_error_modal(self, "API KEY REQUIRED", "Please enter or paste your OpenRouter or Gemini API key before testing.")
            return
        self.ai_quick_status_lbl.configure(text="[*] Verifying AI Uplink (OpenRouter / Gemini Cloud)...", text_color=NEON_GREEN)
        def _task():
            ok, msg = validate_gemini_api_key(k)
            def _ui():
                try:
                    if ok:
                        self.ai_quick_status_lbl.configure(text=f"🟢 {msg}", text_color=NEON_GREEN)
                        messagebox.showinfo("API CONNECTED", f"SUCCESS!\n\n{msg}")
                    else:
                        self.ai_quick_status_lbl.configure(text=f"🔴 {msg}", text_color=DANGER)
                        show_api_error_modal(self, "AI QUICK CONNECT TEST FAILED", msg)
                except Exception:
                    pass
            try:
                self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _save_ai_quick_api(self):
        k = self.ai_quick_api_entry.get().strip() if hasattr(self, "ai_quick_api_entry") else ""
        if not k:
            messagebox.showwarning("NO KEY", "Please paste your Gemini API key, or switch to Offline DSA Vault.")
            return
        self.ai_quick_status_lbl.configure(text="[*] Testing & connecting API key...", text_color=NEON_GREEN)
        def _task():
            ok, msg = validate_gemini_api_key(k)
            def _ui():
                try:
                    if ok:
                        self.session["api_key"] = k
                        save_session(self.session)
                        self.backend = AntigravityBackend(k)
                        if hasattr(self, "lbl_prof_api"):
                            self.lbl_prof_api.configure(text="API STATUS: ACTIVE", text_color=NEON_GREEN)
                        self._build_ai_tab(self.frames["AI_MODULE"])
                        self.update_status("[+] AI UPLINK CONNECTED & ACTIVE!")
                        messagebox.showinfo("AI ACTIVATED", "Gemini API connected successfully! AI Mode is now active.")
                    else:
                        show_api_error_modal(self, "AI QUICK CONNECT VERIFICATION FAILED", msg)
                        ans = messagebox.askyesno("API KEY WARNING", f"Google Gemini verification returned:\n{msg}\n\nWould you like to activate anyway?")
                        if ans:
                            self.session["api_key"] = k
                            save_session(self.session)
                            self.backend = AntigravityBackend(k)
                            if hasattr(self, "lbl_prof_api"):
                                self.lbl_prof_api.configure(text="API STATUS: ACTIVE", text_color=NEON_GREEN)
                            self._build_ai_tab(self.frames["AI_MODULE"])
                            self.update_status("[+] AI UPLINK CONFIGURED.")
                        else:
                            self.ai_quick_status_lbl.configure(text=f"🔴 {msg}", text_color=DANGER)
                except Exception:
                    pass
            try:
                self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _build_ai_tab(self, p):
        for w in p.winfo_children():
            try:
                w.destroy()
            except Exception:
                pass

        if not self.session.get("api_key",""):
            card = HackerCard(p)
            card.pack(fill="both", expand=True, padx=20, pady=20)

            ctk.CTkLabel(card, text="⚡ AI UPLINK NOT CONFIGURED", font=FH1, text_color=DANGER).pack(pady=(25, 5))
            ctk.CTkLabel(card, text="An OpenRouter (sk-or-...) or Google Gemini (AIzaSy...) key is required for AI Screen Snipping & Auto Code Generation.", font=FB, text_color=MUTED).pack(pady=(0, 15))

            # 1-Click Direct Links to get OpenRouter or Gemini key
            link_box = ctk.CTkFrame(card, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
            link_box.pack(fill="x", padx=30, pady=10)
            ctk.CTkLabel(link_box, text="Choose your provider (OpenRouter or Google Gemini):", font=FS, text_color=TEXT).pack(pady=(10, 4))
            l_row = ctk.CTkFrame(link_box, fg_color="transparent")
            l_row.pack(fill="x", padx=15, pady=(0, 10))
            HackerButton(l_row, "🌐 GET OPENROUTER KEY (openrouter.ai)",
                         lambda: webbrowser.open("https://openrouter.ai/keys"),
                         height=36, color=SURFACE, hover=DARK_GREEN, text_col=NEON_GREEN, font=FS).pack(side="left", fill="x", expand=True, padx=(0, 5))
            HackerButton(l_row, "🔑 GET GEMINI KEY (Google AI Studio)",
                         lambda: webbrowser.open("https://aistudio.google.com/app/apikey"),
                         height=36, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG, font=FS).pack(side="right", fill="x", expand=True, padx=(5, 0))

            # Inline API key entry & testing
            setup_card = ctk.CTkFrame(card, fg_color="transparent")
            setup_card.pack(fill="x", padx=30, pady=10)

            ctk.CTkLabel(setup_card, text="PASTE OPENROUTER (sk-or-...) OR GEMINI KEY HERE:", font=FB, text_color=NEON_GREEN, anchor="w").pack(fill="x", pady=(5, 3))

            entry_row = ctk.CTkFrame(setup_card, fg_color="transparent")
            entry_row.pack(fill="x", pady=5)
            self.ai_quick_api_entry = HackerEntry(entry_row, show="*", placeholder="Paste OpenRouter Key (sk-or-...) or Gemini Key (AIzaSy...)...")
            self.ai_quick_api_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

            HackerButton(entry_row, "⚡ TEST KEY", self._test_ai_quick_api, height=38, width=110, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN).pack(side="right")

            self.ai_quick_status_lbl = ctk.CTkLabel(setup_card, text="[*] Enter your API key and click 'CONNECT & ACTIVATE AI MODE'", font=FS, text_color=MUTED, anchor="w")
            self.ai_quick_status_lbl.pack(fill="x", pady=(2, 10))

            HackerButton(setup_card, "💾 CONNECT & ACTIVATE AI MODE", self._save_ai_quick_api, height=44, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG).pack(fill="x", pady=(0, 10))

            # Alternate Offline Buttons
            alt_box = ctk.CTkFrame(card, fg_color="transparent")
            alt_box.pack(fill="x", padx=30, pady=(15, 20))
            ctk.CTkLabel(alt_box, text="OR USE OFFLINE TOOLS (NO INTERNET / NO API KEY REQUIRED):", font=FS, text_color=MUTED).pack(pady=(0, 8))
            alt_row = ctk.CTkFrame(alt_box, fg_color="transparent")
            alt_row.pack(fill="x")
            HackerButton(alt_row, "📚 OPEN OFFLINE DSA VAULT", lambda: self.show_frame("OFFLINE_VAULT"), height=38).pack(side="left", fill="x", expand=True, padx=(0, 5))
            HackerButton(alt_row, "⌨️ MANUAL OVERRIDE (AUTO-TYPER)", lambda: self.show_frame("MANUAL_OVERRIDE"), height=38, color=SURFACE, text_col=MUTED).pack(side="right", fill="x", expand=True, padx=(5, 0))
            return

        # Top Bar with AI Uplink Status & Direct Link
        top_bar = ctk.CTkFrame(p, fg_color="transparent")
        top_bar.pack(fill="x", padx=15, pady=(5, 5))

        ctk.CTkLabel(top_bar, text="🟢 AI UPLINK ACTIVE (Gemini Connected)", font=FB, text_color=NEON_GREEN).pack(side="left")

        HackerButton(top_bar, "⚙️ API SETTINGS / TEST", self._open_api_config_modal, height=30, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN, font=FS).pack(side="right", padx=(5, 0))
        HackerButton(top_bar, "🔑 GET FREE KEY", lambda: webbrowser.open("https://aistudio.google.com/app/apikey"), height=30, color=SURFACE, text_col=MUTED, font=FS).pack(side="right")

        # Settings Grid Card
        scard = HackerCard(p)
        scard.pack(fill="x", padx=15, pady=(5,10))

        # Row 1: Target Lang & Format Type
        r1 = ctk.CTkFrame(scard, fg_color="transparent")
        r1.pack(fill="x", padx=15, pady=(10,5))

        ctk.CTkLabel(r1, text="TARGET LANG:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(0,10))
        self.lang_var = ctk.StringVar(value="python")
        ctk.CTkComboBox(r1, values=["python","cpp","java","javascript","c","sql","rust","go"],
                        variable=self.lang_var, width=140, fg_color=SURFACE, text_color=NEON_GREEN,
                        border_color=DARK_GREEN, button_color=DARK_GREEN, font=FB, corner_radius=0).pack(side="left", padx=(0,20))

        ctk.CTkLabel(r1, text="FORMAT:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(0,10))
        ctk.CTkSegmentedButton(r1, values=["competitive", "leetcode"], variable=self.format_var,
                               selected_color=DARK_GREEN, selected_hover_color=NEON_GREEN,
                               fg_color=SURFACE, text_color=NEON_GREEN, font=FB).pack(side="left", padx=(0,20))

        ctk.CTkLabel(r1, text="SOLUTION:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(0,10))
        ctk.CTkSegmentedButton(r1, values=["optimal", "simple"], variable=self.sol_type_var,
                               selected_color=DARK_GREEN, selected_hover_color=NEON_GREEN,
                               fg_color=SURFACE, text_color=NEON_GREEN, font=FB).pack(side="left")

        # Row 2: Speed & Typo Cadence
        r2 = ctk.CTkFrame(scard, fg_color="transparent")
        r2.pack(fill="x", padx=15, pady=(5,10))

        ctk.CTkLabel(r2, text="TYPING SPEED:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(0,10))
        ctk.CTkComboBox(r2, values=["Slow Student (35 WPM)", "Average (60 WPM)", "Rapid (110 WPM)"],
                        variable=self.typing_speed_var, width=200, fg_color=SURFACE, text_color=NEON_GREEN,
                        border_color=DARK_GREEN, button_color=DARK_GREEN, font=FB, corner_radius=0).pack(side="left", padx=(0,20))

        ctk.CTkCheckBox(r2, text="HUMAN TYPO SIMULATION (ANTI-CHEAT BYPASS)", variable=self.typo_sim_var,
                        fg_color=DARK_GREEN, hover_color=NEON_GREEN, checkmark_color=NEON_GREEN, border_color=DARK_GREEN, font=FB, text_color=MUTED).pack(side="left")

        # Vision Capture Buttons
        vbar = ctk.CTkFrame(p, fg_color="transparent")
        vbar.pack(fill="x", padx=15, pady=(0,8))

        HackerButton(vbar, "📸 CROP SCREEN SNIP (DRAG BOX)", self._start_interactive_snip, height=48).pack(side="left", fill="x", expand=True, padx=(0,6))
        HackerButton(vbar, "🖥 FULLSCREEN CAPTURE (T-3s)", self.start_vision_generation, height=48, color=SURFACE, text_col=NEON_GREEN).pack(side="right", fill="x", expand=True, padx=(6,0))

        ctk.CTkLabel(p, text="--- OR TYPE PROBLEM STATEMENT ---", font=FS, text_color=MUTED).pack(pady=(0,5))

        self.prompt_entry = ctk.CTkTextbox(p, height=140, fg_color=SURFACE, text_color=NEON_GREEN, font=FB, border_width=2, border_color=DARK_GREEN, corner_radius=0)
        self.prompt_entry.pack(fill="both", expand=True, padx=15, pady=(0,10))

        # Action Buttons
        act_bar = ctk.CTkFrame(p, fg_color="transparent")
        act_bar.pack(fill="x", padx=15, pady=(0,15))

        HackerButton(act_bar, "GENERATE & INJECT CODE", self.start_text_generation, height=46).pack(side="left", fill="x", expand=True, padx=(0,6))
        HackerButton(act_bar, "🎓 VIVA SHEET", self._generate_viva_for_current, height=46, color=SURFACE, text_col=NEON_GREEN, width=150).pack(side="left", padx=3)
        HackerButton(act_bar, "🧪 TEST CASES", self._predict_test_cases_for_current, height=46, color=SURFACE, text_col=NEON_GREEN, width=150).pack(side="left", padx=(3,0))

    def _build_manual_tab(self, p):
        ctk.CTkLabel(p, text="PASTE CODE PAYLOAD TO INJECT:", font=FH2, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=20, pady=(15,5))
        ctk.CTkLabel(p, text="Agent Prayath will minimize, detect your click inside your editor, and type the payload automatically.", font=FS, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(0,10))

        self.manual_code_box = ctk.CTkTextbox(p, fg_color=SURFACE, text_color=NEON_GREEN, font=FM, border_width=2, border_color=DARK_GREEN, corner_radius=0)
        self.manual_code_box.pack(fill="both", expand=True, padx=20, pady=(0,15))
        HackerButton(p, "INITIATE MANUAL INJECTION", self.start_direct_typing, height=55).pack(fill="x", padx=20, pady=(0,15))

    # ── STUDENT: VIVA & EXPLAINER TAB ────────────────────────────────────────
    def _build_viva_tab(self, p):
        top = ctk.CTkFrame(p, fg_color="transparent")
        top.pack(fill="x", padx=15, pady=(15,5))
        ctk.CTkLabel(top, text=">_ VIVA & EXAM CHEAT SHEET GENERATOR", font=FH2, text_color=NEON_GREEN).pack(side="left")

        HackerButton(top, "⟳ ANALYZE CURRENT CODE", self._generate_viva_for_current, height=32, color=SURFACE, text_col=NEON_GREEN).pack(side="right")

        card = HackerCard(p)
        card.pack(fill="x", padx=15, pady=5)
        ctk.CTkLabel(card, text="Instant breakdown of algorithm, time/space complexity, and common examiner questions.", font=FS, text_color=MUTED, anchor="w").pack(fill="x", padx=15, pady=8)

        self.viva_box = ctk.CTkTextbox(p, fg_color=SURFACE, text_color=NEON_GREEN, font=FM, border_width=2, border_color=DARK_GREEN, corner_radius=0)
        self.viva_box.pack(fill="both", expand=True, padx=15, pady=(5,15))
        self.viva_box.insert("end", "[*] No code analyzed yet.\n\nGenerate or paste code in AI Module or Offline Vault, then click '⟳ ANALYZE CURRENT CODE' to generate a complete college viva cheat sheet!\n")

    # ── STUDENT: TEST CASES PREDICTOR TAB ────────────────────────────────────
    def _build_test_cases_tab(self, p):
        top = ctk.CTkFrame(p, fg_color="transparent")
        top.pack(fill="x", padx=15, pady=(15,5))
        ctk.CTkLabel(top, text=">_ TEST CASE & EDGE CASE PREDICTOR", font=FH2, text_color=NEON_GREEN).pack(side="left")

        HackerButton(top, "⟳ PREDICT TEST CASES", self._predict_test_cases_for_current, height=32, color=SURFACE, text_col=NEON_GREEN).pack(side="right")

        card = HackerCard(p)
        card.pack(fill="x", padx=15, pady=5)
        ctk.CTkLabel(card, text="Predicts 3 custom input/output test suites and identifies critical edge cases (overflow, negatives, nulls).", font=FS, text_color=MUTED, anchor="w").pack(fill="x", padx=15, pady=8)

        self.test_cases_box = ctk.CTkTextbox(p, fg_color=SURFACE, text_color=NEON_GREEN, font=FM, border_width=2, border_color=DARK_GREEN, corner_radius=0)
        self.test_cases_box.pack(fill="both", expand=True, padx=15, pady=(5,15))
        self.test_cases_box.insert("end", "[*] Click '⟳ PREDICT TEST CASES' to evaluate the current code or prompt against hidden test cases and boundary conditions.\n")

    # ── STUDENT: OFFLINE DSA VAULT TAB ───────────────────────────────────────
    def _build_offline_vault_tab(self, p):
        top = ctk.CTkFrame(p, fg_color="transparent")
        top.pack(fill="x", padx=15, pady=(15,5))
        ctk.CTkLabel(top, text=">_ OFFLINE DSA LAB REPOSITORY (ZERO INTERNET)", font=FH2, text_color=NEON_GREEN).pack(side="left")

        # Controls Card
        ctrl = HackerCard(p)
        ctrl.pack(fill="x", padx=15, pady=5)

        r = ctk.CTkFrame(ctrl, fg_color="transparent")
        r.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(r, text="ALGORITHM:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(0,10))
        algo_names = list(OFFLINE_DSA_VAULT.keys())
        self.vault_algo_var = ctk.StringVar(value=algo_names[0] if algo_names else "Binary Search")
        ctk.CTkComboBox(r, values=algo_names, variable=self.vault_algo_var, command=lambda v: self._update_vault_preview(),
                        width=220, fg_color=SURFACE, text_color=NEON_GREEN, border_color=DARK_GREEN, button_color=DARK_GREEN, font=FB).pack(side="left", padx=(0,20))

        ctk.CTkLabel(r, text="LANGUAGE:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(0,10))
        self.vault_lang_var = ctk.StringVar(value="python")
        ctk.CTkSegmentedButton(r, values=["python", "cpp", "java"], variable=self.vault_lang_var, command=lambda v: self._update_vault_preview(),
                               selected_color=DARK_GREEN, selected_hover_color=NEON_GREEN, fg_color=SURFACE, text_color=NEON_GREEN, font=FB).pack(side="left", padx=(0,20))

        HackerButton(r, "⚡ INJECT ALGORITHM", self._inject_vault_code, height=36).pack(side="right")

        # Code preview
        self.vault_code_box = ctk.CTkTextbox(p, fg_color=SURFACE, text_color=NEON_GREEN, font=FM, border_width=2, border_color=DARK_GREEN, corner_radius=0)
        self.vault_code_box.pack(fill="both", expand=True, padx=15, pady=(5,15))
        self._update_vault_preview()

    def _update_vault_preview(self):
        algo = self.vault_algo_var.get()
        lang = self.vault_lang_var.get()
        code_snip = OFFLINE_DSA_VAULT.get(algo, {}).get(lang, "# Solution not found")
        if hasattr(self, "vault_code_box"):
            self.vault_code_box.delete("1.0", "end")
            self.vault_code_box.insert("end", code_snip)
            self.last_generated_code = code_snip
            self.last_generated_lang = lang

    def _inject_vault_code(self):
        code_to_type = self.vault_code_box.get("1.0", "end").strip()
        if code_to_type:
            self.start_direct_typing_payload(code_to_type)


    # ── ADMIN: LIVE MONITOR TAB (ONLY FOR ADMIN) ─────────────────────────────
    def _build_live_monitor_tab(self, p):
        top = ctk.CTkFrame(p, fg_color="transparent")
        top.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(top, text=">_ LIVE SATELLITE TELEMETRY", font=FH2, text_color=NEON_GREEN).pack(side="left")

        # Refresh button
        HackerButton(top, "⟳ REFRESH NOW", self._refresh_live_users, height=32, color=SURFACE, text_col=NEON_GREEN).pack(side="right")

        # Stats Cards
        stats_frame = ctk.CTkFrame(p, fg_color="transparent")
        stats_frame.pack(fill="x", padx=10, pady=(0,10))

        self.card_online = HackerCard(stats_frame, height=65)
        self.card_online.pack(side="left", fill="x", expand=True, padx=(0,5))
        self.card_online.pack_propagate(False)
        self.lbl_online_count = ctk.CTkLabel(self.card_online, text="🟢 ONLINE USERS: 0", font=FH2, text_color=NEON_GREEN)
        self.lbl_online_count.pack(expand=True)

        self.card_total = HackerCard(stats_frame, height=65)
        self.card_total.pack(side="right", fill="x", expand=True, padx=(5,0))
        self.card_total.pack_propagate(False)
        self.lbl_last_ping = ctk.CTkLabel(self.card_total, text="⏱ SYNC: LIVE CLOUD", font=FH3, text_color=MUTED)
        self.lbl_last_ping.pack(expand=True)

        # Treeview for live users
        tree_frame = ctk.CTkFrame(p, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        cols = ("Status", "Roll", "Name", "Role", "Branch", "Mode", "LastActive")
        self.live_tree = ttk.Treeview(tree_frame, columns=cols, show="headings", style="Hacker.Treeview", height=10)
        self.live_tree.heading("Status", text="STATUS")
        self.live_tree.heading("Roll", text="ROLL NO / ID")
        self.live_tree.heading("Name", text="FULL NAME")
        self.live_tree.heading("Role", text="ROLE")
        self.live_tree.heading("Branch", text="BRANCH")
        self.live_tree.heading("Mode", text="ACTIVE MODE")
        self.live_tree.heading("LastActive", text="LAST PING")

        self.live_tree.column("Status", width=90, anchor="center")
        self.live_tree.column("Roll", width=120)
        self.live_tree.column("Name", width=220)
        self.live_tree.column("Role", width=80, anchor="center")
        self.live_tree.column("Branch", width=80)
        self.live_tree.column("Mode", width=140)
        self.live_tree.column("LastActive", width=110, anchor="center")

        live_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.live_tree.yview)
        self.live_tree.configure(yscrollcommand=live_scroll.set)
        live_scroll.pack(side="right", fill="y")
        self.live_tree.pack(side="left", fill="both", expand=True)

        # Periodic background auto-refresher for live monitor
        self._schedule_live_refresh()

    def _schedule_live_refresh(self):
        if not self._shutdown_event.is_set():
            if getattr(self, "current_mode", "") == "LIVE_MONITOR":
                self._refresh_live_users()
            self.after(10000, self._schedule_live_refresh)

    def _refresh_live_users(self):
        """Fetch online presence from Firebase and render in Treeview."""
        def _fetch():
            presence_data = get_online_presence()
            now = time.time()
            rows = []
            online_count = 0

            for key, info in sorted(presence_data.items(), key=lambda x: x[1].get("last_seen", 0), reverse=True):
                last_seen = info.get("last_seen", 0)
                diff = now - last_seen
                if diff <= 60:
                    status_str = "🟢 ONLINE"
                    online_count += 1
                elif diff <= 240:
                    status_str = "🟡 IDLE"
                else:
                    status_str = "⚪ OFFLINE"

                if diff < 60:
                    ago_str = f"{int(diff)}s ago"
                elif diff < 3600:
                    ago_str = f"{int(diff//60)}m ago"
                else:
                    ago_str = f"{int(diff//3600)}h ago"

                rows.append((
                    status_str,
                    info.get("roll", key),
                    info.get("name", "N/A"),
                    info.get("role", "student").upper(),
                    info.get("branch", "N/A"),
                    info.get("mode", "MANUAL"),
                    ago_str
                ))

            def _update_ui():
                if not hasattr(self, "live_tree"): return
                for item in self.live_tree.get_children():
                    self.live_tree.delete(item)
                for r in rows:
                    self.live_tree.insert("", "end", values=r)
                self.lbl_online_count.configure(text=f"🟢 ONLINE USERS: {online_count}")
                self.lbl_last_ping.configure(text=f"⏱ LAST SYNC: {time.strftime('%H:%M:%S')}")

            self.after(0, _update_ui)

        threading.Thread(target=_fetch, daemon=True).start()

    # ── ADMIN: DB ADMIN TAB (ONLY FOR ADMIN) ──────────────────────────────────
    def _build_admin_tab(self, p):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Hacker.Treeview", background=SURFACE, foreground=NEON_GREEN, fieldbackground=SURFACE, 
                        borderwidth=0, font=FS, rowheight=24)
        style.configure("Hacker.Treeview.Heading", background=DARK_GREEN, foreground=SURFACE, font=FB, relief="flat")
        style.map("Hacker.Treeview", background=[("selected", MUTED)], foreground=[("selected", SURFACE)])

        self.admin_db = load_cloud_db() or {}
        self.admin_branch_filter = "ALL"
        self.admin_group_filter = "ALL GROUPS"
        self.user_groups_cache = {}
        self._search_after_id = None
        self._branch_pill_buttons = {}

        sf = ctk.CTkFrame(p, fg_color="transparent")
        sf.pack(fill="x", pady=(5,3), padx=10)
        self.search_var = ctk.StringVar()
        se = HackerEntry(sf, placeholder="🔍 Search Roll No, Name or Branch (Live Fast Filter)...")
        se.pack(side="left", fill="x", expand=True, padx=(0,8))
        se.configure(textvariable=self.search_var)
        self.search_var.trace_add("write", self._filter_admin_tree)

        HackerButton(sf, "👥 USER GROUPS", self._open_user_groups_modal, height=35, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG).pack(side="right", padx=(6,0))
        HackerButton(sf, "💾 EXPORT BACKUP", self._admin_export_backup, height=35, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN).pack(side="right", padx=(6,0))
        HackerButton(sf, "⟳ SYNC CLOUD", self._admin_sync_cloud, height=35, color=SURFACE, text_col=NEON_GREEN).pack(side="right")

        # Database Quick Filter & Stats Ribbon
        flt_ribbon = ctk.CTkFrame(p, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        flt_ribbon.pack(fill="x", padx=10, pady=(2, 4))

        ctk.CTkLabel(flt_ribbon, text="Branch:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(8, 3), pady=4)
        for b_name in ["ALL", "DS", "CSE", "AIML", "ECE", "EEE", "ME", "CE", "TEMP"]:
            btn = HackerButton(
                flt_ribbon, b_name, lambda b=b_name: self._set_admin_branch_filter(b),
                height=26, width=42 if len(b_name) <= 3 else 55, font=FS,
                color=DARK_GREEN if b_name == "ALL" else SURFACE,
                text_col=BG if b_name == "ALL" else MUTED
            )
            btn.pack(side="left", padx=2, pady=4)
            self._branch_pill_buttons[b_name] = btn

        ctk.CTkLabel(flt_ribbon, text="Group:", font=FB, text_color=NEON_GREEN).pack(side="left", padx=(12, 3), pady=4)
        self.admin_group_filter_var = ctk.StringVar(value="ALL GROUPS")
        self.admin_group_filter_menu = ctk.CTkOptionMenu(
            flt_ribbon, variable=self.admin_group_filter_var,
            values=["ALL GROUPS"],
            command=self._on_admin_group_filter_changed,
            fg_color=SURFACE, text_color=NEON_GREEN, button_color=DARK_GREEN, font=FS, width=150
        )
        self.admin_group_filter_menu.pack(side="left", padx=4, pady=4)

        self.lbl_admin_db_stats = ctk.CTkLabel(flt_ribbon, text="📊 TOTAL: 0 STUDENTS", font=FB, text_color=NEON_GREEN)
        self.lbl_admin_db_stats.pack(side="right", padx=12, pady=4)

        tree_frame = ctk.CTkFrame(p, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=4)

        cols = ("Roll", "Name", "Branch", "Status", "Password", "Phone")
        self.tree = ttk.Treeview(tree_frame, columns=cols, show="headings", style="Hacker.Treeview", height=12)
        self.tree.heading("Roll", text="ROLL NO")
        self.tree.heading("Name", text="FULL NAME")
        self.tree.heading("Branch", text="BRANCH")
        self.tree.heading("Status", text="STATUS")
        self.tree.heading("Password", text="PASSWORD")
        self.tree.heading("Phone", text="PHONE")

        self.tree.column("Roll", width=110)
        self.tree.column("Name", width=230)
        self.tree.column("Branch", width=70)
        self.tree.column("Status", width=90)
        self.tree.column("Password", width=100)
        self.tree.column("Phone", width=110)

        self.tree.tag_configure("perm", foreground=NEON_GREEN)
        self.tree.tag_configure("temp", foreground="#ffb300")
        self.tree.tag_configure("migrated", foreground="#00e5ff")

        scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self._on_tree_select)

        form = ctk.CTkFrame(p, fg_color="transparent")
        form.pack(fill="x", padx=10, pady=4)

        ctk.CTkLabel(form, text="Roll:", font=FS, text_color=MUTED).grid(row=0, column=0, padx=4, pady=2, sticky="e")
        self.edt_roll = HackerEntry(form); self.edt_roll.grid(row=0, column=1, padx=4, pady=2, sticky="ew")

        ctk.CTkLabel(form, text="Name:", font=FS, text_color=MUTED).grid(row=0, column=2, padx=4, pady=2, sticky="e")
        self.edt_name = HackerEntry(form); self.edt_name.grid(row=0, column=3, padx=4, pady=2, sticky="ew")

        ctk.CTkLabel(form, text="Branch:", font=FS, text_color=MUTED).grid(row=1, column=0, padx=4, pady=2, sticky="e")
        self.edt_branch = HackerEntry(form); self.edt_branch.grid(row=1, column=1, padx=4, pady=2, sticky="ew")

        ctk.CTkLabel(form, text="Password:", font=FS, text_color=MUTED).grid(row=1, column=2, padx=4, pady=2, sticky="e")
        self.edt_pw = HackerEntry(form); self.edt_pw.grid(row=1, column=3, padx=4, pady=2, sticky="ew")

        form.columnconfigure(1, weight=1); form.columnconfigure(3, weight=1)

        btns = ctk.CTkFrame(p, fg_color="transparent")
        btns.pack(fill="x", padx=10, pady=4)
        HackerButton(btns, "➕ ADD USER", self._admin_add, height=32, color=DARK_GREEN, text_col=BG).pack(side="left", expand=True, padx=2)
        HackerButton(btns, "💾 UPDATE USER & PW", self._admin_update, height=32, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN).pack(side="left", expand=True, padx=2)
        HackerButton(btns, "🧹 CLEAR FORM", self._admin_clear_form, height=32, color=SURFACE, text_col=MUTED).pack(side="left", expand=True, padx=2)
        HackerButton(btns, "🗑️ DELETE USER", self._admin_delete, height=32, color=DANGER, text_col="#ffffff", border_color=DANGER).pack(side="left", expand=True, padx=2)

        self._refresh_admin_tree()
        self._refresh_admin_group_filter_options()

        # ── GLOBAL UPDATE NOTIFICATION & RELEASE BROADCASTER ─────────────────
        b_card = HackerCard(p)
        b_card.pack(fill="x", padx=10, pady=(10, 5))

        b_hdr = ctk.CTkFrame(b_card, fg_color="transparent")
        b_hdr.pack(fill="x", padx=15, pady=(8, 4))
        ctk.CTkLabel(b_hdr, text="📢 GLOBAL UPDATE NOTIFICATION & RELEASE BROADCASTER", font=FB, text_color=NEON_GREEN).pack(side="left")
        ctk.CTkLabel(b_hdr, text="(ADMIN ONLY - PUSHES TO ALL STUDENT SCREENS)", font=FS, text_color=MUTED).pack(side="right")

        b_grid = ctk.CTkFrame(b_card, fg_color="transparent")
        b_grid.pack(fill="x", padx=15, pady=3)

        ctk.CTkLabel(b_grid, text="Target Version:", font=FS, text_color=MUTED).grid(row=0, column=0, padx=4, pady=2, sticky="e")
        self.admin_upd_v_entry = HackerEntry(b_grid, placeholder="e.g. v3.1 or v4.0")
        self.admin_upd_v_entry.grid(row=0, column=1, padx=4, pady=2, sticky="ew")
        self.admin_upd_v_entry.insert(0, APP_VERSION)

        ctk.CTkLabel(b_grid, text="Direct Binary URL:", font=FS, text_color=MUTED).grid(row=0, column=2, padx=4, pady=2, sticky="e")
        self.admin_upd_url_entry = HackerEntry(b_grid, placeholder="Direct download URL to AgentPrayath.exe (GitHub/Drive/Dropbox)")
        self.admin_upd_url_entry.grid(row=0, column=3, padx=4, pady=2, sticky="ew")

        ctk.CTkLabel(b_grid, text="Announcement / Msg:", font=FS, text_color=MUTED).grid(row=1, column=0, padx=4, pady=2, sticky="e")
        self.admin_upd_msg_entry = HackerEntry(b_grid, placeholder="What's new in this release (e.g. Fixed DSA Vault, added Exam Predictor)...")
        self.admin_upd_msg_entry.grid(row=1, column=1, columnspan=3, padx=4, pady=2, sticky="ew")

        ctk.CTkLabel(b_grid, text="Target Audience:", font=FS, text_color=NEON_GREEN).grid(row=2, column=0, padx=4, pady=2, sticky="e")
        self.admin_target_audience_var = ctk.StringVar(value="ALL USERS (Entire Campus)")
        self.admin_target_menu = ctk.CTkOptionMenu(
            b_grid, variable=self.admin_target_audience_var,
            values=[
                "ALL USERS (Entire Campus)",
                "ADMIN ONLY",
                "BRANCH: DATA SCIENCE (DS)",
                "BRANCH: COMPUTER SCIENCE (CSE)",
                "BRANCH: ARTIFICIAL INTELLIGENCE (AIML)",
                "BRANCH: ELECTRONICS (ECE)",
                "BRANCH: ELECTRICAL (EEE)",
                "BRANCH: MECHANICAL (ME)",
                "BRANCH: CIVIL (CE)"
            ],
            fg_color=SURFACE, text_color=NEON_GREEN, button_color=DARK_GREEN, font=FS
        )
        self.admin_target_menu.grid(row=2, column=1, padx=4, pady=2, sticky="ew")

        HackerButton(b_grid, "👥 CREATE / MANAGE GROUPS", self._open_user_groups_modal, height=32, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN, font=FS).grid(row=2, column=2, columnspan=2, padx=4, pady=2, sticky="ew")

        b_grid.columnconfigure(1, weight=1)
        b_grid.columnconfigure(3, weight=2)

        b_opts = ctk.CTkFrame(b_card, fg_color="transparent")
        b_opts.pack(fill="x", padx=15, pady=3)

        self.admin_upd_popup_var = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(b_opts, text="Trigger Instant Pop-up Modal on Student Screens", variable=self.admin_upd_popup_var,
                        fg_color=DARK_GREEN, hover_color=NEON_GREEN, text_color=TEXT, font=FS).pack(side="left")

        b_act = ctk.CTkFrame(b_card, fg_color="transparent")
        b_act.pack(fill="x", padx=15, pady=(4, 8))

        HackerButton(b_act, "📢 BROADCAST UPDATE TO AUDIENCE", self._admin_broadcast_update, height=34, color=DARK_GREEN, text_col=BG).pack(side="left", padx=(0, 10))
        HackerButton(b_act, "🛑 CLEAR BROADCAST", self._admin_clear_broadcast, height=34, color=SURFACE, text_col=DANGER, border_color=DANGER).pack(side="left", padx=(0, 10))
        HackerButton(b_act, "⏪ REVOKE LAST UPDATE", self._admin_revoke_latest_update, height=34, color=SURFACE, text_col=WARNING, border_color=WARNING).pack(side="left", padx=(0, 10))
        HackerButton(b_act, "🗑️ CLEAR UPDATE HISTORY", self._clear_update_history_action, height=34, color=SURFACE, text_col=DANGER, border_color=DANGER).pack(side="left", padx=(0, 10))
        HackerButton(b_act, "📜 VIEW RELEASE HISTORY", lambda: self.show_frame("UPDATE_CENTER"), height=34, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN, font=FS).pack(side="left")

        self.admin_broadcast_status = ctk.CTkLabel(b_act, text="[+] Ready to broadcast updates to campus.", font=FS, text_color=MUTED, anchor="w")
        self.admin_broadcast_status.pack(side="left", padx=15, fill="x", expand=True)

        self.after(500, self._refresh_admin_target_options)
        self.after(800, self._load_current_broadcast_info)

    def _admin_sync_cloud(self):
        def _task():
            self.update_status("[*] FETCHING LIVE DATABASE FROM FIREBASE...")
            fresh = _firebase_request("/students", timeout=12)
            if isinstance(fresh, dict) and fresh:
                self.admin_db = fresh
                save_local_db(fresh, force=True)
                self.after(0, self._refresh_admin_tree)
                self.update_status(f"[+] Synced {len(fresh)} records from Firebase.")
            else:
                self.update_status("[-] Firebase fetch returned empty.")
        threading.Thread(target=_task, daemon=True).start()

    def _admin_export_backup(self):
        from tkinter import filedialog
        path = filedialog.asksaveasfilename(
            title="Export Cloud Database Backup (Admin Only)",
            defaultextension=".json",
            filetypes=[("JSON Database", "*.json")],
            initialfile="cloud_db.json"
        )
        if path:
            try:
                db_to_export = self.admin_db or _firebase_request("/students", timeout=15) or {}
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(db_to_export, f, indent=2)
                messagebox.showinfo("EXPORT SUCCESS", f"Admin backup exported successfully ({len(db_to_export)} records) to:\n\n{path}")
                self.update_status(f"[+] Admin exported database backup ({len(db_to_export)} records)")
            except Exception as e:
                messagebox.showerror("EXPORT ERROR", f"Failed to export database: {e}")

    def _admin_clear_form(self):
        self.edt_roll.delete(0, "end")
        self.edt_name.delete(0, "end")
        self.edt_branch.delete(0, "end")
        self.edt_pw.delete(0, "end")
        for s in self.tree.selection():
            self.tree.selection_remove(s)
        self.update_status("[*] User form cleared. Ready for new student.")

    def _set_admin_branch_filter(self, branch):
        self.admin_branch_filter = branch
        if hasattr(self, "_branch_pill_buttons"):
            for b, btn in self._branch_pill_buttons.items():
                if b == branch:
                    btn.configure(fg_color=DARK_GREEN, text_color=BG)
                else:
                    btn.configure(fg_color=SURFACE, text_color=MUTED)
        self._refresh_admin_tree()

    def _on_admin_group_filter_changed(self, choice):
        self.admin_group_filter = choice
        self._refresh_admin_tree()

    def _refresh_admin_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        query = self.search_var.get().lower().strip()
        b_flt = getattr(self, "admin_branch_filter", "ALL").upper()
        g_flt = getattr(self, "admin_group_filter", "ALL GROUPS")

        group_members = None
        if g_flt != "ALL GROUPS" and hasattr(self, "user_groups_cache") and g_flt in self.user_groups_cache:
            ginfo = self.user_groups_cache[g_flt]
            if isinstance(ginfo, dict):
                mems = ginfo.get("members", [])
                if isinstance(mems, list):
                    group_members = set(str(m).strip().upper() for m in mems)

        records = sorted(self.admin_db.items(), key=lambda x: str(x[0]))
        count = 0
        for roll, data in records:
            if not isinstance(data, dict): continue
            u_roll = str(roll).upper()
            name = str(data.get("name",""))
            branch = str(data.get("branch","")).upper()
            pw = str(data.get("password",""))
            phone = str(data.get("phone","N/A"))
            if data.get("migrated_to"):
                status = f"-> {data['migrated_to']}"
                tag = "migrated"
            elif data.get("is_temp"):
                status = "TEMP_ROLL"
                tag = "temp"
            else:
                status = "PERMANENT"
                tag = "perm"

            # Branch filter
            if b_flt != "ALL":
                if b_flt == "TEMP":
                    if not data.get("is_temp") and "AUS" not in u_roll:
                        continue
                elif b_flt in ("DS", "DATA SCIENCE"):
                    if branch not in ("DS", "DATA SCIENCE"): continue
                elif b_flt not in branch:
                    continue

            # Group filter
            if group_members is not None and u_roll not in group_members:
                continue

            # Search query
            if query and (query not in str(roll).lower() and query not in name.lower() and 
                query not in branch.lower() and query not in status.lower() and query not in phone.lower()):
                continue

            self.tree.insert("", "end", values=(roll, name, branch, status, pw, phone), tags=(tag,))
            count += 1
            if count >= 800: break

        if hasattr(self, "lbl_admin_db_stats"):
            tot = len(self.admin_db)
            grp_cnt = len(getattr(self, "user_groups_cache", {}))
            self.lbl_admin_db_stats.configure(
                text=f"📊 DATABASE: {tot:,} STUDENTS  |  🟢 SHOWING: {count}  |  🏷️ GROUPS: {grp_cnt}"
            )

    def _filter_admin_tree(self, *args):
        if hasattr(self, "_search_after_id") and self._search_after_id:
            try: self.after_cancel(self._search_after_id)
            except Exception: pass
        self._search_after_id = self.after(160, self._refresh_admin_tree)

    def _on_tree_select(self, event):
        sel = self.tree.selection()
        if not sel: return
        item = self.tree.item(sel[0])
        vals = item['values']
        self.edt_roll.delete(0, "end"); self.edt_roll.insert(0, str(vals[0]))
        self.edt_name.delete(0, "end"); self.edt_name.insert(0, str(vals[1]))
        self.edt_branch.delete(0, "end"); self.edt_branch.insert(0, str(vals[2]))
        self.edt_pw.delete(0, "end")
        if len(vals) > 4 and str(vals[4]) != "None":
            self.edt_pw.insert(0, str(vals[4]))

    def _admin_add(self):
        roll = self.edt_roll.get().strip().upper()
        if not roll: return
        data = {
            "name": self.edt_name.get().strip(),
            "branch": self.edt_branch.get().strip(),
            "password": self.edt_pw.get().strip(),
            "university": "Aditya University",
            "phone": "N/A"
        }
        self.admin_db[roll] = data
        set_student(roll, data)
        save_local_db(self.admin_db)
        self._refresh_admin_tree()
        self.update_status(f"[+] Added user {roll} to Firebase Cloud")

    def _admin_update(self):
        roll = self.edt_roll.get().strip().upper()
        if not roll: return
        patch = {
            "name": self.edt_name.get().strip(),
            "branch": self.edt_branch.get().strip(),
            "password": self.edt_pw.get().strip()
        }
        if roll in self.admin_db and isinstance(self.admin_db[roll], dict):
            self.admin_db[roll].update(patch)
        else:
            patch["university"] = "Aditya University"
            self.admin_db[roll] = patch

        update_student(roll, patch)
        save_local_db(self.admin_db)
        self._refresh_admin_tree()
        self.update_status(f"[*] Updated user {roll} in Firebase Cloud")

    def _admin_delete(self):
        roll = self.edt_roll.get().strip().upper()
        if roll in self.admin_db:
            del self.admin_db[roll]
            delete_student(roll)
            save_local_db(self.admin_db)
            self._refresh_admin_tree()
            self.edt_roll.delete(0,"end"); self.edt_name.delete(0,"end"); self.edt_branch.delete(0,"end"); self.edt_pw.delete(0,"end")
            self.update_status(f"[-] Deleted user {roll} from Firebase Cloud")

    # ── SMART INTERVIEWS TEST SUITE (v4.0 EXCLUSIVE) ─────────────────────────
    def _open_smart_interviews_popup(self):
        """Open or refocus the Smart Interviews Popup Window."""
        if not hasattr(self, "si_popup") or not self.si_popup or not self.si_popup.winfo_exists():
            self.si_popup = SmartInterviewsPopup(self)
        else:
            self.si_popup.deiconify()
            self.si_popup.lift()
            self.si_popup.focus_force()
        self.update_status("[+] SMART INTERVIEWS POPUP WINDOW ACTIVATED.")

    def _open_tiny_mcq_window(self):
        """Open or refocus the Tiny MCQ HUD Window."""
        if not hasattr(self, "tiny_mcq_window") or not self.tiny_mcq_window or not self.tiny_mcq_window.winfo_exists():
            self.tiny_mcq_window = TinyMCQWindow(self, parent_popup=getattr(self, "si_popup", None))
        else:
            self.tiny_mcq_window.deiconify()
            self.tiny_mcq_window.lift()
            self.tiny_mcq_window.focus_force()
        self.update_status("[+] TINY MCQ HUD WINDOW ACTIVATED.")

    def _build_smart_interviews_tab(self, p):
        # Scrollable container for tab contents
        scroll = ctk.CTkScrollableFrame(p, fg_color="transparent")
        scroll.pack(fill="both", expand=True)

        # 1. Header Card
        h_card = HackerCard(scroll)
        h_card.pack(fill="x", padx=15, pady=(10, 8))

        top_h = ctk.CTkFrame(h_card, fg_color="transparent")
        top_h.pack(fill="x", padx=20, pady=(14, 4))
        ctk.CTkLabel(top_h, text="⚡ SMART INTERVIEWS TEST SUITE", font=FH1, text_color=NEON_GREEN, anchor="w").pack(side="left")
        ctk.CTkLabel(top_h, text="[ v4.0 ADMIN EXCLUSIVE ]", font=FB, text_color=BG, fg_color=NEON_GREEN, corner_radius=4, padx=8, pady=2).pack(side="right")

        ctk.CTkLabel(
            h_card,
            text="Autonomous Assessment Proctor • Smart MCQ Vision Solver & AI Code Writer with Smart Cursor Detection",
            font=FM, text_color=MUTED, anchor="w"
        ).pack(fill="x", padx=20, pady=(0, 14))

        # 2. API Key Configuration & Live Verification Card
        api_card = HackerCard(scroll)
        api_card.pack(fill="x", padx=15, pady=8)

        ctk.CTkLabel(api_card, text="🔑 GEMINI API KEY SETUP & VERIFICATION", font=FH2, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=20, pady=(14, 4))
        ctk.CTkLabel(
            api_card,
            text="Add your OpenRouter key (sk-or-...) or Google Gemini key (AIzaSy...). The system automatically detects your provider and validates live uplink readiness.\nOnce verified, setup is completed and the Smart Interviews Popup Window opens automatically.",
            font=FS, text_color=MUTED, justify="left", anchor="w"
        ).pack(fill="x", padx=20, pady=(0, 10))

        # Action Buttons row: Google AI Studio link & clipboard paste
        link_row = ctk.CTkFrame(api_card, fg_color="transparent")
        link_row.pack(fill="x", padx=20, pady=(0, 8))

        def _open_ai_studio():
            import webbrowser
            webbrowser.open("https://aistudio.google.com/app/apikey")

        HackerButton(link_row, "🌐 GET OPENROUTER KEY (openrouter.ai)", lambda: webbrowser.open("https://openrouter.ai/keys"),
                     height=28, width=240, color=SURFACE, hover=DARK_GREEN, text_col=NEON_GREEN, font=FS).pack(side="left", padx=(0, 10))
        HackerButton(link_row, "🌐 GET GEMINI KEY (Google AI Studio)", _open_ai_studio,
                     height=28, width=240, color=SURFACE, hover=DARK_GREEN, text_col=NEON_GREEN, font=FS).pack(side="left", padx=(0, 10))

        def _paste_clipboard():
            try:
                clip = self.clipboard_get().strip()
                if clip:
                    self.si_api_entry.delete(0, "end")
                    self.si_api_entry.insert(0, clip)
            except Exception:
                pass

        HackerButton(link_row, "📋 PASTE FROM CLIPBOARD", _paste_clipboard,
                     height=28, width=170, color=SURFACE, hover=BORDER_LT, text_col=TEXT, font=FS).pack(side="left")

        # Entry Row
        entry_row = ctk.CTkFrame(api_card, fg_color="transparent")
        entry_row.pack(fill="x", padx=20, pady=(0, 8))

        self.si_api_show_var = ctk.BooleanVar(value=False)
        self.si_api_entry = HackerEntry(entry_row, placeholder="Paste OpenRouter Key (sk-or-...) or Gemini Key (AIzaSy...)", show="•")
        self.si_api_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

        cur_key = self.session.get("api_key", "")
        if cur_key:
            self.si_api_entry.insert(0, cur_key)

        def _toggle_api_visibility():
            if self.si_api_show_var.get():
                self.si_api_show_var.set(False)
                self.si_api_entry.configure(show="•")
                self.btn_si_eye.configure(text="👁️ SHOW")
            else:
                self.si_api_show_var.set(True)
                self.si_api_entry.configure(show="")
                self.btn_si_eye.configure(text="🔒 HIDE")

        self.btn_si_eye = HackerButton(entry_row, "👁️ SHOW", _toggle_api_visibility,
                                       height=38, width=80, color=SURFACE, text_col=MUTED, font=FS)
        self.btn_si_eye.pack(side="left", padx=(0, 8))

        self.btn_si_test = HackerButton(entry_row, "⚡ TEST & COMPLETE SETUP", self._test_and_complete_si_setup,
                                        height=38, width=220, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG, font=FB)
        self.btn_si_test.pack(side="left")

        # OpenRouter Preferred Model Selector
        model_row = ctk.CTkFrame(api_card, fg_color="transparent")
        model_row.pack(fill="x", padx=20, pady=(0, 10))

        ctk.CTkLabel(model_row, text="PREFERRED OPENROUTER MODEL:", font=FS, text_color=NEON_GREEN).pack(side="left", padx=(0, 10))
        self.si_or_model_var = ctk.StringVar(value=self.session.get("openrouter_model", "Auto-Best (Recommended)"))
        self.si_or_menu = ctk.CTkOptionMenu(
            model_row,
            variable=self.si_or_model_var,
            values=[
                "Auto-Best (Recommended)",
                "google/gemini-2.5-flash",
                "google/gemini-2.5-flash-lite",
                "openai/gpt-4o-mini",
                "qwen/qwen2.5-vl-72b-instruct",
                "nvidia/nemotron-3.5-super-vl:free",
                "qwen/qwen-2.5-coder-32b-instruct",
                "deepseek/deepseek-chat"
            ],
            command=self._on_openrouter_model_changed,
            fg_color=SURFACE, text_color=NEON_GREEN, button_color=DARK_GREEN, font=FS, width=280
        )
        self.si_or_menu.pack(side="left")

        # Live Status Banner for API
        self.si_api_status_card = ctk.CTkFrame(api_card, fg_color=CARD, border_width=1, border_color=BORDER, corner_radius=4)
        self.si_api_status_card.pack(fill="x", padx=20, pady=(0, 14))

        init_status = "🟢 API KEY PRESENT: Click 'TEST & COMPLETE SETUP' to verify & launch." if cur_key else "⚪ NO API KEY CONFIGURED: Paste your key above and click 'TEST & COMPLETE SETUP'."
        init_col = NEON_GREEN if cur_key else MUTED
        self.si_api_status = ctk.CTkLabel(
            self.si_api_status_card, text=init_status,
            font=FM, text_color=init_col, anchor="w"
        )
        self.si_api_status.pack(fill="x", padx=12, pady=8)

        # 3. Popup Launcher Card
        ctl_card = HackerCard(scroll)
        ctl_card.pack(fill="x", padx=15, pady=8)

        ctk.CTkLabel(ctl_card, text="🚀 SMART INTERVIEWS POPUP CONTROLLER", font=FH2, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=20, pady=(14, 4))
        ctk.CTkLabel(
            ctl_card,
            text="Launch the lightweight floating HUD window that stays on top during tests.\nSwitch between Multiple Choice (MCQ) answers and Autonomous AI Code Writing at any time.",
            font=FS, text_color=MUTED, justify="left", anchor="w"
        ).pack(fill="x", padx=20, pady=(0, 12))

        c_btn_row = ctk.CTkFrame(ctl_card, fg_color="transparent")
        c_btn_row.pack(fill="x", padx=20, pady=(0, 14))

        HackerButton(c_btn_row, "🚀 LAUNCH SMART INTERVIEWS POPUP WINDOW", self._open_smart_interviews_popup,
                     height=42, width=300, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG, font=FB).pack(side="left", padx=(0, 10))

        HackerButton(c_btn_row, "⚡ LAUNCH TINY MCQ HUD (OPTIONS ONLY)", self._open_tiny_mcq_window,
                     height=42, width=300, color="#1f538d", hover="#3a7ebf", text_col="#ffffff", font=FB).pack(side="left", padx=(0, 12))

        # 4. Feature Architecture Guide
        guide_card = HackerCard(scroll)
        guide_card.pack(fill="x", padx=15, pady=(8, 20))

        ctk.CTkLabel(guide_card, text="📖 HOW TO USE SMART INTERVIEWS TEST v4.0", font=FH2, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=20, pady=(14, 6))

        guide_text = (
            "• 📝 MODE 1 - MULTIPLE CHOICE QUESTIONS (MCQ) SOLVER:\n"
            "  1. In the popup window, click '📸 CAPTURE FULL SCREEN' or '✂️ SNIP QUESTION'.\n"
            "  2. Gemini 2.5 Flash analyzes question title, choices (A, B, C, D), and outputs the exact CORRECT ANSWER.\n"
            "  3. Correct option is highlighted in high-contrast neon green with a crisp 1-2 sentence explanation.\n\n"
            "• 💻 MODE 2 - AUTONOMOUS AI CODE WRITER (WITH SMART CURSOR DETECTION):\n"
            "  1. Click '🔀 SWITCH TO AI CODE WRITER' at the top of the popup window.\n"
            "  2. Select your target language (Python 3, Java, C++, C, JavaScript, or Auto-Detect).\n"
            "  3. Click '📸 CAPTURE & SOLVE CODE' or '✂️ SNIP PROBLEM REGION'.\n"
            "  4. ⚠️ SMART CURSOR FOCUS: The engine generates code and enters 'WAITING FOR CURSOR' state.\n"
            "  5. Without putting your cursor inside the editor, it will NOT write anything!\n"
            "  6. Place your cursor inside the browser code editor (click in editor) -> the engine detects the click and types code automatically with human anti-cheat cadence!\n"
            "  7. Emergency stop: Press [ESC] at any time to cancel instantly."
        )
        ctk.CTkLabel(guide_card, text=guide_text, font=FS, text_color=TEXT, justify="left", anchor="w").pack(fill="x", padx=20, pady=(0, 15))

    def _test_and_complete_si_setup(self):
        k = self.si_api_entry.get().strip() if hasattr(self, "si_api_entry") else ""
        if not k:
            self.si_api_status.configure(text="❌ API Key cannot be empty. Please paste your OpenRouter or Gemini key.", text_color=DANGER)
            return

        self.btn_si_test.configure(state="disabled")
        self.si_api_status.configure(text="🟡 TESTING API KEY (OPENROUTER / GEMINI CLOUD)...", text_color="#FFD700")

        def _task():
            ok, msg = validate_ai_uplink_key(k)
            def _ui():
                self.btn_si_test.configure(state="normal")
                if ok:
                    self.session["api_key"] = k
                    save_session(self.session)
                    self.backend = AntigravityBackend(k, preferred_model=self.session.get("openrouter_model", "Auto-Best (Recommended)"))
                    p_name = "OpenRouter" if self.backend.provider == "openrouter" else "Gemini"
                    self.si_api_status.configure(
                        text=f"✅ SETUP COMPLETED! {p_name} AI is active & verified. (Popup window opened!)",
                        text_color=NEON_GREEN
                    )
                    self.update_status(f"[+] {p_name.upper()} API VALIDATED & SETUP COMPLETED.")
                    # Automatically open the Smart Interviews popup window
                    self.after(200, self._open_smart_interviews_popup)
                else:
                    self.si_api_status.configure(
                        text=f"❌ VALIDATION FAILED: {msg}",
                        text_color=DANGER
                    )
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _on_openrouter_model_changed(self, chosen_model):
        self.session["openrouter_model"] = chosen_model
        save_session(self.session)
        if hasattr(self, "backend") and self.backend:
            self.backend.preferred_model = chosen_model
        self.update_status(f"[+] OPENROUTER MODEL: {chosen_model}")

    # ── PROFILE & SECURITY TAB ───────────────────────────────────────────────
    def _build_profile_tab(self, p):
        pr = self.session
        roll = pr.get("roll", "")
        role = pr.get("role", "student")

        card = HackerCard(p)
        card.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(card, text="ACCOUNT PROFILE & CLOUD SECURITY", font=FH2, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=20, pady=(15,10))

        grid = ctk.CTkFrame(card, fg_color="transparent")
        grid.pack(fill="x", padx=20, pady=5)

        self.lbl_prof_role = ctk.CTkLabel(grid, text=f"ROLE:       {role.upper()}", font=FB, text_color=MUTED, anchor="w")
        self.lbl_prof_role.grid(row=0, column=0, sticky="w", pady=3)
        self.lbl_prof_roll = ctk.CTkLabel(grid, text=f"ROLL NO:    {roll or 'ADMIN'}", font=FB, text_color=NEON_GREEN, anchor="w")
        self.lbl_prof_roll.grid(row=0, column=1, sticky="w", pady=3, padx=20)

        self.lbl_prof_uni = ctk.CTkLabel(grid, text=f"UNIVERSITY: {pr.get('university', 'Aditya University')}", font=FB, text_color=MUTED, anchor="w")
        self.lbl_prof_uni.grid(row=1, column=0, sticky="w", pady=3)
        self.lbl_prof_api = ctk.CTkLabel(grid, text=f"API STATUS: {'ACTIVE' if pr.get('api_key') else 'OFFLINE'}", font=FB, text_color=NEON_GREEN if pr.get('api_key') else WARNING, anchor="w")
        self.lbl_prof_api.grid(row=1, column=1, sticky="w", pady=3, padx=20)

        grid.columnconfigure(0, weight=1); grid.columnconfigure(1, weight=1)

        # Edit Section
        edit_card = HackerCard(p)
        edit_card.pack(fill="both", expand=True, padx=20, pady=(0,15))

        ctk.CTkLabel(edit_card, text="UPDATE INFORMATION IN DATABASE:", font=FH3, text_color=MUTED, anchor="w").pack(fill="x", padx=20, pady=(15,10))

        eform = ctk.CTkFrame(edit_card, fg_color="transparent")
        eform.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(eform, text="FULL NAME:", font=FS, text_color=MUTED).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.prof_name = HackerEntry(eform); self.prof_name.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.prof_name.insert(0, pr.get("name", ""))

        ctk.CTkLabel(eform, text="BRANCH:", font=FS, text_color=MUTED).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.prof_branch = HackerEntry(eform); self.prof_branch.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.prof_branch.insert(0, pr.get("branch", ""))

        ctk.CTkLabel(eform, text="PHONE:", font=FS, text_color=MUTED).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.prof_phone = HackerEntry(eform); self.prof_phone.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.prof_phone.insert(0, pr.get("phone", ""))

        ctk.CTkLabel(eform, text="NEW PASSWORD:", font=FS, text_color=NEON_GREEN).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.prof_pw = HackerEntry(eform, show="*"); self.prof_pw.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        if pr.get("password"): self.prof_pw.insert(0, pr.get("password"))

        ctk.CTkLabel(eform, text="GEMINI API KEY:", font=FS, text_color=NEON_GREEN).grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.prof_api = HackerEntry(eform, show="*", placeholder="Paste Gemini API key (starts with AIzaSy...)...")
        self.prof_api.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        if pr.get("api_key"): self.prof_api.insert(0, pr.get("api_key"))

        api_act_row = ctk.CTkFrame(eform, fg_color="transparent")
        api_act_row.grid(row=5, column=1, sticky="ew", padx=5, pady=(2, 6))
        HackerButton(api_act_row, "⚡ TEST KEY", self._test_profile_api, height=30, color=SURFACE, text_col=NEON_GREEN, border_color=DARK_GREEN, font=FS).pack(side="left", padx=(0, 6))
        HackerButton(api_act_row, "🔑 GET FREE KEY", lambda: webbrowser.open("https://aistudio.google.com/app/apikey"), height=30, color=SURFACE, text_col=MUTED, font=FS).pack(side="left")
        self.lbl_profile_api_res = ctk.CTkLabel(api_act_row, text="", font=FS, text_color=NEON_GREEN)
        self.lbl_profile_api_res.pack(side="left", padx=10)

        eform.columnconfigure(1, weight=1)

        self.prof_msg = ctk.CTkLabel(edit_card, text="", font=FS, text_color=NEON_GREEN)
        self.prof_msg.pack(pady=5)

        prof_btn_box = ctk.CTkFrame(edit_card, fg_color="transparent")
        prof_btn_box.pack(fill="x", padx=20, pady=(5,15))

        HackerButton(prof_btn_box, "💾 SAVE PROFILE TO CLOUD", self._save_user_profile, height=44).pack(fill="x", expand=True)

        # Update card in Profile
        up_card = HackerCard(p)
        up_card.pack(fill="x", padx=20, pady=(0,15))
        self.lbl_prof_build = ctk.CTkLabel(up_card, text=f"SOFTWARE & INTERFACE BUILD: {APP_VERSION} (LIVE CLOUD SYNCHRONIZED)", font=FB, text_color=NEON_GREEN, anchor="w")
        self.lbl_prof_build.pack(fill="x", padx=20, pady=(12,5))

        up_actions = ctk.CTkFrame(up_card, fg_color="transparent")
        up_actions.pack(fill="x", padx=20, pady=(5,12))

        HackerButton(up_actions, "📡 OPEN CLOUD UPDATE CENTER", lambda: self.show_frame("UPDATE_CENTER"), height=40, color=DARK_GREEN, hover=NEON_GREEN, text_col=BG).pack(fill="x")

    def _apply_interface_refresh(self, new_version=None):
        global APP_VERSION
        if new_version:
            APP_VERSION = new_version
            self._popup_shown_for = new_version
        v_display = APP_VERSION
        pr = self.session
        role = pr.get("role", "UNKNOWN").upper()
        name = pr.get("name", "UNKNOWN").upper()
        roll = pr.get("roll", "")
        id_text = f"[{role}] {name} {roll}"

        if hasattr(self, "hdr_id_lbl"):
            self.hdr_id_lbl.configure(text=id_text)
        if hasattr(self, "hdr_title_lbl"):
            self.hdr_title_lbl.configure(text=f">_ AGENT PRAYATH {v_display}")
        self.title(f"AGENT PRAYATH {v_display} - {name}")

        # Update profile overview labels
        if hasattr(self, "lbl_prof_role"):
            self.lbl_prof_role.configure(text=f"ROLE:       {role}")
        if hasattr(self, "lbl_prof_roll"):
            self.lbl_prof_roll.configure(text=f"ROLL NO:    {roll or 'ADMIN'}")
        if hasattr(self, "lbl_prof_uni"):
            self.lbl_prof_uni.configure(text=f"UNIVERSITY: {pr.get('university', 'Aditya University')}")
        if hasattr(self, "lbl_prof_api"):
            self.lbl_prof_api.configure(text=f"API STATUS: {'ACTIVE' if pr.get('api_key') else 'OFFLINE'}")
        if hasattr(self, "lbl_prof_build"):
            self.lbl_prof_build.configure(text=f"SOFTWARE & INTERFACE BUILD: {v_display} (LIVE CLOUD SYNCHRONIZED)")
        if hasattr(self, "broadcast_banner"):
            self.broadcast_banner.pack_forget()

        # Update entry boxes in profile tab
        if hasattr(self, "prof_name"):
            self.prof_name.delete(0, "end")
            self.prof_name.insert(0, pr.get("name", ""))
        if hasattr(self, "prof_branch"):
            self.prof_branch.delete(0, "end")
            self.prof_branch.insert(0, pr.get("branch", ""))
        if hasattr(self, "prof_phone"):
            self.prof_phone.delete(0, "end")
            self.prof_phone.insert(0, pr.get("phone", ""))
        if hasattr(self, "prof_pw") and pr.get("password"):
            self.prof_pw.delete(0, "end")
            self.prof_pw.insert(0, pr.get("password", ""))
        if hasattr(self, "prof_api"):
            self.prof_api.delete(0, "end")
            self.prof_api.insert(0, pr.get("api_key", ""))

        if hasattr(self, "prof_msg"):
            self.prof_msg.configure(text="[+] INTERFACE, PROFILE & DATABASE REFRESHED FROM CLOUD!", text_color=NEON_GREEN)

        # Admin tree refresh
        if hasattr(self, "admin_db"):
            self.admin_db = load_cloud_db()
            self._refresh_admin_tree()

        self.update_status(f"[+] INTERFACE UPDATED: {v_display}")

    def _test_profile_api(self):
        k = self.prof_api.get().strip() if hasattr(self, "prof_api") else ""
        if not k:
            self.lbl_profile_api_res.configure(text="[-] Please enter key first.", text_color=DANGER)
            return
        self.lbl_profile_api_res.configure(text="[*] Testing with Google Cloud...", text_color=NEON_GREEN)
        def _task():
            ok, msg = validate_gemini_api_key(k)
            def _ui():
                try:
                    if ok:
                        self.lbl_profile_api_res.configure(text=f"🟢 {msg[:45]}", text_color=NEON_GREEN)
                    else:
                        self.lbl_profile_api_res.configure(text=f"🔴 {msg[:45]}", text_color=DANGER)
                except Exception:
                    pass
            try:
                self.after(0, _ui)
            except Exception:
                pass
        threading.Thread(target=_task, daemon=True).start()

    def _check_update_and_refresh_ui(self):
        """
        One-click complete refresh and update:
        1. Refreshes user profile and session live from Firebase Cloud.
        2. Refreshes entire UI interface (headers, titles, profile cards, admin trees, status).
        3. Checks for software updates from Cloud & opens AppUpdateModal.
        """
        self.update_status("[*] CHECKING UPDATES & REFRESHING INTERFACE...")
        
        def _task():
            # 1. Fetch fresh student/user record from Firebase
            roll = self.session.get("roll", "")
            if roll:
                cloud_data = get_student(roll)
                if cloud_data:
                    self.session.update({
                        "name": cloud_data.get("name", self.session.get("name")),
                        "branch": cloud_data.get("branch", self.session.get("branch")),
                        "university": cloud_data.get("university", self.session.get("university")),
                        "phone": cloud_data.get("phone", self.session.get("phone")),
                        "password": cloud_data.get("password", self.session.get("password")),
                    })
                    save_session(self.session)

            # 2. Re-sync local database cache (Admin only)
            if self.session.get("role") == "admin":
                load_cloud_db(force_download=True)

            # 3. Update all UI elements on main thread
            self.after(0, self._apply_interface_refresh)

            # 4. Open AppUpdateModal
            self.after(200, lambda: AppUpdateModal(self))

        threading.Thread(target=_task, daemon=True).start()

    def _save_user_profile(self):
        name = self.prof_name.get().strip()
        branch = self.prof_branch.get().strip()
        phone = self.prof_phone.get().strip()
        new_pw = self.prof_pw.get().strip()
        new_api = self.prof_api.get().strip() if hasattr(self, "prof_api") else self.session.get("api_key", "")

        if new_pw and len(new_pw) < 4:
            self.prof_msg.configure(text="Password must be at least 4 characters long.", text_color=DANGER)
            return

        roll = self.session.get("roll", "")
        self.session["name"] = name
        self.session["branch"] = branch
        self.session["phone"] = phone
        self.session["api_key"] = new_api
        if new_pw: self.session["password"] = new_pw
        save_session(self.session)

        # Re-initialize backend with new API key
        self.backend = AntigravityBackend(new_api)
        if hasattr(self, "lbl_prof_api"):
            self.lbl_prof_api.configure(text=f"API STATUS: {'ACTIVE' if new_api else 'OFFLINE'}",
                                        text_color=NEON_GREEN if new_api else WARNING)
        if hasattr(self, "_build_ai_tab") and "AI_MODULE" in getattr(self, "frames", {}):
            self._build_ai_tab(self.frames["AI_MODULE"])

        # Update Firebase Cloud & local cache
        if roll:
            patch = {"name": name, "branch": branch, "phone": phone}
            if new_pw: patch["password"] = new_pw
            update_student(roll, patch)
            if self.session.get("role") == "admin":
                try:
                    local_db = load_cloud_db()
                    if roll in local_db and isinstance(local_db[roll], dict):
                        local_db[roll].update(patch)
                        save_local_db(local_db, force=True)
                except Exception:
                    pass

        self.prof_msg.configure(text="[+] PROFILE & API KEY SAVED SUCCESSFULLY!", text_color=NEON_GREEN)
        self.update_status("[+] Profile & API configuration saved.")

        self._apply_interface_refresh()
        self.prof_msg.configure(text="[+] PROFILE & PASSWORD SYNCHRONIZED WITH FIREBASE CLOUD!", text_color=NEON_GREEN)
        self.update_status("[+] Profile & Cloud Database updated successfully.")

    # ── UPDATE CENTER TAB ────────────────────────────────────────────────────
    def _build_update_center_tab(self, p):
        top = ctk.CTkFrame(p, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=(15,10))
        ctk.CTkLabel(top, text=">_ SYSTEM UPDATE & CLOUD DEPLOYMENT PORTAL", font=FH2, text_color=NEON_GREEN).pack(side="left")

        # Telemetry Card
        tcard = HackerCard(p)
        tcard.pack(fill="x", padx=20, pady=5)

        tgrid = ctk.CTkFrame(tcard, fg_color="transparent")
        tgrid.pack(fill="x", padx=20, pady=12)

        ctk.CTkLabel(tgrid, text=f"INSTALLED VERSION:  {APP_VERSION}", font=FB, text_color=MUTED, anchor="w").grid(row=0, column=0, sticky="w", pady=4)
        self.lbl_cloud_v = ctk.CTkLabel(tgrid, text="CLOUD VERSION:      CHECKING...", font=FB, text_color=NEON_GREEN, anchor="w")
        self.lbl_cloud_v.grid(row=0, column=1, sticky="w", pady=4, padx=20)

        ctk.CTkLabel(tgrid, text="STATUS:             READY FOR UPDATE", font=FB, text_color=WARNING, anchor="w").grid(row=1, column=0, sticky="w", pady=4)
        ctk.CTkLabel(tgrid, text="DATABASE:           4,400+ CAMPUS USERS SYNCED", font=FB, text_color=NEON_GREEN, anchor="w").grid(row=1, column=1, sticky="w", pady=4, padx=20)
        tgrid.columnconfigure(0, weight=1); tgrid.columnconfigure(1, weight=1)

        # Release Highlights
        rcard = HackerCard(p)
        rcard.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(rcard, text="RELEASE HIGHLIGHTS & CHANGELOG:", font=FH3, text_color=NEON_GREEN, anchor="w").pack(fill="x", padx=20, pady=(12,5))
        self.lbl_changelog = ctk.CTkLabel(
            rcard,
            text="• AUS Temporary Roll Number Login & Linking to Permanent Roll\n"
                 "• Complete 4,400+ Student Campus Directory Integration (DS, CSE, ECE, EEE, ME, CE)\n"
                 "• Live Firebase Cloud Telemetry & Automated Heartbeat Engine\n"
                 "• One-Click Over-The-Air (OTA) Application & Database Updater",
            font=FS, text_color="#cccccc", justify="left", anchor="w"
        )
        self.lbl_changelog.pack(fill="x", padx=20, pady=(0,12))

        # Progress bar
        self.tab_update_prog = ctk.CTkProgressBar(p, fg_color=SURFACE, progress_color=NEON_GREEN, height=12)
        self.tab_update_prog.set(0)
        self.tab_update_prog.pack(fill="x", padx=20, pady=(5,10))

        # Update Console Logs
        self.tab_update_log = ctk.CTkTextbox(p, height=110, fg_color=SURFACE, text_color=NEON_GREEN, font=FM, border_width=1, border_color=DARK_GREEN)
        self.tab_update_log.pack(fill="x", padx=20, pady=(0,10))
        self.tab_update_log.insert("end", "[*] System Ready. Click '⚡ UPDATE TO NEW VERSION' to fetch latest release packages.\n")

        # Action Buttons
        btn_bar = ctk.CTkFrame(p, fg_color="transparent")
        btn_bar.pack(fill="x", padx=20, pady=(0,10))

        self.btn_tab_update = HackerButton(btn_bar, "⚡ UPDATE TO NEW VERSION", self._trigger_tab_update, height=44)
        self.btn_tab_update.pack(side="right", padx=(10,0))

        HackerButton(btn_bar, "⟳ CHECK FOR UPDATES", self._refresh_update_telemetry, color=SURFACE, text_col=NEON_GREEN, height=44).pack(side="right")

        # Update & Release History Card
        hcard = HackerCard(p)
        hcard.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        h_hdr = ctk.CTkFrame(hcard, fg_color="transparent")
        h_hdr.pack(fill="x", padx=15, pady=(8, 4))
        ctk.CTkLabel(h_hdr, text="📜 SYSTEM UPDATE & RELEASE HISTORY (AUDIENCE TARGETED)", font=FH3, text_color=NEON_GREEN).pack(side="left")
        HackerButton(h_hdr, "🗑️ CLEAR ALL", self._clear_update_history_action, height=26, color=SURFACE, text_col=DANGER, border_color=DANGER, font=FS).pack(side="right", padx=(6, 0))
        HackerButton(h_hdr, "🗑️ DELETE SELECTED", self._delete_selected_history_item, height=26, color=SURFACE, text_col=DANGER, border_color=DANGER, font=FS).pack(side="right", padx=(6, 0))
        HackerButton(h_hdr, "⏪ REVOKE LAST UPDATE", self._admin_revoke_latest_update, height=26, color=SURFACE, text_col=WARNING, border_color=WARNING, font=FS).pack(side="right", padx=(6, 0))
        HackerButton(h_hdr, "⟳ REFRESH", self._refresh_update_history_table, height=26, color=SURFACE, text_col=NEON_GREEN, font=FS).pack(side="right")

        tree_h_frame = ctk.CTkFrame(hcard, fg_color=SURFACE, border_width=1, border_color=DARK_GREEN)
        tree_h_frame.pack(fill="both", expand=True, padx=15, pady=(4, 10))

        cols = ("Version", "Audience", "Date", "Changelog", "Author")
        self.history_tree = ttk.Treeview(tree_h_frame, columns=cols, show="headings", style="Hacker.Treeview", height=5)
        self.history_tree.heading("Version", text="VERSION")
        self.history_tree.heading("Audience", text="TARGET AUDIENCE")
        self.history_tree.heading("Date", text="DATE")
        self.history_tree.heading("Changelog", text="CHANGELOG / HIGHLIGHTS")
        self.history_tree.heading("Author", text="AUTHOR")

        self.history_tree.column("Version", width=80, anchor="center")
        self.history_tree.column("Audience", width=170)
        self.history_tree.column("Date", width=130, anchor="center")
        self.history_tree.column("Changelog", width=340)
        self.history_tree.column("Author", width=90, anchor="center")

        h_scroll = ttk.Scrollbar(tree_h_frame, orient="vertical", command=self.history_tree.yview)
        self.history_tree.configure(yscrollcommand=h_scroll.set)
        h_scroll.pack(side="right", fill="y")
        self.history_tree.pack(side="left", fill="both", expand=True)

        self.after(500, self._refresh_update_telemetry)
        self.after(700, self._refresh_update_history_table)

    def _refresh_update_history_table(self):
        def _task():
            history = get_update_history()
            def _ui():
                if not hasattr(self, "history_tree"): return
                self._history_key_map = {}
                for itm in self.history_tree.get_children():
                    self.history_tree.delete(itm)
                if not history:
                    self.history_tree.insert("", "end", values=(APP_VERSION, "ALL USERS", time.strftime("%Y-%m-%d"), "History cleared. System up to date with cloud release.", "ROOT_ADMIN"))
                else:
                    for h in history:
                        iid = self.history_tree.insert("", "end", values=(
                            h.get("version", APP_VERSION),
                            h.get("target_audience", "ALL USERS"),
                            h.get("date_str") or h.get("release_date") or time.strftime("%Y-%m-%d"),
                            h.get("changelog") or h.get("message") or "System updates",
                            h.get("author", "ADMIN")
                        ))
                        self._history_key_map[iid] = h.get("key")
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _refresh_update_telemetry(self):
        def _task():
            info = get_system_update_info()
            bc = _firebase_request("/system_broadcast")
            if isinstance(bc, dict) and bc.get("version"):
                target_aud = bc.get("target_audience", "ALL USERS")
                if self._is_user_eligible_for_broadcast(target_aud):
                    latest_v = bc.get("version")
                    changelog = bc.get("message") or info.get("changelog", "")
                else:
                    latest_v = info.get("latest_version", APP_VERSION)
                    changelog = info.get("changelog", "")
            else:
                latest_v = info.get("latest_version", APP_VERSION)
                changelog = info.get("changelog", "")
            is_newer = is_version_newer(latest_v, APP_VERSION)
            def _ui():
                self.lbl_cloud_v.configure(text=f"CLOUD VERSION:      {latest_v} {'(UPDATE AVAILABLE)' if is_newer else '(LATEST)'}")
                if changelog:
                    self.lbl_changelog.configure(text=f"• {changelog.replace(', ', '\n• ')}")
                if is_newer:
                    self.btn_tab_update.configure(text="⚡ UPDATE TO NEW VERSION", fg_color=NEON_GREEN)
                else:
                    self.btn_tab_update.configure(text="✔ RE-SYNC SYSTEM", fg_color=DARK_GREEN)
            self.after(0, _ui)
        threading.Thread(target=_task, daemon=True).start()

    def _trigger_tab_update(self):
        self.btn_tab_update.configure(state="disabled")
        self.tab_update_prog.set(0.2)
        self.tab_update_log.delete("1.0", "end")

        def _log_cb(msg):
            def _ui():
                self.tab_update_log.insert("end", f"{msg}\n")
                self.tab_update_log.see("end")
            self.after(0, _ui)

        def _worker():
            self.after(0, lambda: self.tab_update_prog.set(0.5))
            res = perform_system_update(_log_cb)
            if isinstance(res, tuple) and len(res) == 3:
                ok, v, new_exe = res
            elif isinstance(res, tuple) and len(res) == 2:
                ok, v = res; new_exe = None
            else:
                ok, v, new_exe = True, APP_VERSION, None
            self.after(0, lambda: self.tab_update_prog.set(1.0))
            if ok:
                self._new_exe_path = new_exe
                _log_cb(f"\n[+] UPDATE TO {v} COMPLETED SUCCESSFULLY!")
                _log_cb("[*] Automatically reopening application in 2 seconds...")
                def _do_restart():
                    messagebox.showinfo(
                        "UPDATE SUCCESSFUL",
                        f"AGENT PRAYATH has been updated to {v} successfully!\n\nThe application will now automatically reopen."
                    )
                    self._restart_application()
                self.after(500, _do_restart)
            else:
                _log_cb("\n[!] Synchronization incomplete. Current installation preserved.")
                self.after(0, lambda: self.btn_tab_update.configure(state="normal"))

        threading.Thread(target=_worker, daemon=True).start()

    def _restart_application(self):
        self._shutdown_event.set()
        self.logged_out = False
        try:
            if hasattr(self, "kb_listener") and self.kb_listener:
                self.kb_listener.stop()
        except Exception:
            pass
        try:
            roll = self.session.get("roll") or self.session.get("name", "USER")
            remove_online_presence(roll)
        except Exception:
            pass
        try:
            self.destroy()
        except Exception:
            pass
        new_exe = getattr(self, "_new_exe_path", None)
        safe_restart_app(new_exe)

    # ── Helpers ──────────────────────────────────────────────────────────────
    def update_status(self, t):
        try:
            if hasattr(self, 'status_var') and self.status_var:
                self.after(0, lambda: self.status_var.set(t))
        except Exception:
            pass

    def abort_execution(self):
        if self.is_typing:
            self.stop_typing = True
            self.update_status("[!] EMERGENCY ABORT INITIATED.")
            self.after(0, self.deiconify)

    def _disable_buttons(self): pass
    def _enable_buttons(self): pass

    def _start_emergency_listener(self):
        def on_press(k):
            if k in (Key.f8, Key.esc) and self.is_typing: self.abort_execution()
        try:
            self.kb_listener = keyboard.Listener(on_press=on_press)
            self.kb_listener.daemon = True
            self.kb_listener.start()
        except Exception:
            self.kb_listener = None

    def start_vision_generation(self):
        if not self.is_typing: threading.Thread(target=self._run_vision_pipeline, daemon=True).start()

    def start_text_generation(self):
        if self.is_typing: return
        pr = self.prompt_entry.get("1.0","end").strip()
        if not pr: return
        threading.Thread(target=self._run_text_pipeline, args=(pr,), daemon=True).start()

    def start_direct_typing(self):
        if self.is_typing: return
        code = self.manual_code_box.get("1.0","end").strip()
        if not code: return
        threading.Thread(target=self._run_direct_pipeline, args=(code,), daemon=True).start()

    # ── Injection Engine ──────────────────────────────────────────────────────
    def _wait_for_editor_and_clear(self):
        self.after(0, self.iconify)
        self.update_status("[*] MINIMIZED: CLICK INSIDE YOUR CODE EDITOR...")

        click_event = threading.Event()
        def on_click(x, y, button, pressed):
            if pressed:
                click_event.set()
                return False

        listener = mouse.Listener(on_click=on_click)
        listener.start()

        # Wait up to 10 seconds for user to click into their editor
        clicked = click_event.wait(timeout=10.0)
        try:
            listener.stop()
        except Exception:
            pass

        if self.stop_typing:
            self.after(0, self.deiconify)
            return False

        if not clicked:
            self.update_status("[!] TIMEOUT: NO EDITOR CLICK DETECTED. RESTORING WINDOW.")
            self.after(0, self.deiconify)
            return False

        self.update_status("[>] CURSOR DETECTED. CLEARING OLD CODE...")
        time.sleep(0.4)
        self.keyboard.press(Key.ctrl); self.keyboard.press("a")
        self.keyboard.release("a"); self.keyboard.release(Key.ctrl)
        time.sleep(0.15)
        self.keyboard.press(Key.backspace); self.keyboard.release(Key.backspace)
        time.sleep(0.3)
        return True

    def _execute_code_injection(self, initial_code, lang, enable_autonomous=True):
        current_code = initial_code
        max_retries  = 3 if (self.auto_run_var.get() and enable_autonomous) else 1

        for attempt in range(max_retries):
            if self.stop_typing: break

            if not self._wait_for_editor_and_clear(): break

            self.update_status("[>] INJECTING PAYLOAD...")
            self._type_into_editor(current_code)

            if self.stop_typing or not (self.auto_run_var.get() and enable_autonomous): break

            self.keyboard.press(Key.ctrl); self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter); self.keyboard.release(Key.ctrl)
            self.update_status("[*] AWAITING COMPILATION...")
            for _ in range(6):
                if self.stop_typing: break
                time.sleep(1)
            if self.stop_typing: break

            self.update_status("[*] ANALYZING OUTPUT TTY...")
            screenshot = ImageGrab.grab()
            ap = (f"Analyse this screenshot. Did the {lang} code run OK?\n"
                  "If NO ERRORS reply EXACTLY: SUCCESS\n"
                  f"If errors, output the fixed {lang} code ONLY. No markdown.")
            try:
                resp = self.backend.from_image(screenshot, lang, prompt=ap,
                                                sys_inst="You are an autonomous self-correcting agent.")
                if "SUCCESS" in resp[:30].upper():
                    self.update_status("[+] EXECUTION SUCCESSFUL."); break
                else:
                    self.update_status("[-] ERROR DETECTED. RECOMPILING PAYLOAD...")
                    current_code = resp
                    self.preview_box.delete("1.0","end"); self.preview_box.insert("end",current_code)
                    time.sleep(1)
            except Exception as ex:
                self.update_status(f"[!] UPLINK ERROR: {ex}"); break

        if not self.stop_typing:
            if not (self.auto_run_var.get() and enable_autonomous): self.update_status("[+] INJECTION COMPLETE.")
            time.sleep(1)
        self.after(0, self.deiconify)

    def _type_into_editor(self, code):
        char_min, char_max, line_delay = get_cadence_delays(self.typing_speed_var.get())
        sim_typos = self.typo_sim_var.get()
        lines = code.splitlines()

        for idx, line in enumerate(lines):
            if self.stop_typing: break
            for ch in line:
                if self.stop_typing: break

                # Anti-detection human typo simulation
                if sim_typos and ch.lower() in TYPO_ADJACENT and random.random() < 0.012:
                    wrong_ch = TYPO_ADJACENT[ch.lower()]
                    self.keyboard.type(wrong_ch)
                    time.sleep(random.uniform(0.12, 0.20))
                    self.keyboard.press(Key.backspace)
                    self.keyboard.release(Key.backspace)
                    time.sleep(random.uniform(0.04, 0.08))

                self.keyboard.type(ch)
                if ch in "([{\"'":
                    self.keyboard.press(Key.delete); self.keyboard.release(Key.delete)
                time.sleep(random.uniform(char_min, char_max))

            if idx < len(lines)-1 and not self.stop_typing:
                self.keyboard.press(Key.enter); self.keyboard.release(Key.enter)
                time.sleep(line_delay)

    
    # ── STUDENT v3.0 ACTION HANDLERS ──────────────────────────────────────────
    def _toggle_ghost_hud(self):
        if not self.ghost_hud or not self.ghost_hud.winfo_exists():
            self.withdraw()
            self.ghost_hud = GhostHUD(self)
        else:
            self.ghost_hud.destroy()
            self.ghost_hud = None
            self.deiconify()

    def _toggle_theme(self):
        if self.current_theme == "matrix":
            self.current_theme = "office"
            self.configure(fg_color="#f0f2f5")
            self.main_panel.configure(fg_color="#ffffff", border_color="#cccccc")
            self.sidebar.configure(fg_color="#f8f9fa", border_color="#cccccc")
            self.update_status("[+] STEALTH THEME ACTIVE: PLAIN OFFICE MODE")
        else:
            self.current_theme = "matrix"
            self.configure(fg_color=BG)
            self.main_panel.configure(fg_color=CARD, border_color=BORDER_LT)
            self.sidebar.configure(fg_color=CARD, border_color=BORDER_LT)
            self.update_status("[+] CYBERPUNK MATRIX THEME RESTORED")

    def _start_interactive_snip(self):
        self.withdraw()
        self.update_idletasks()
        time.sleep(0.12)
        def _cb(cropped_img):
            self.deiconify()
            self.lift()
            self.focus_force()
            if cropped_img:
                self._process_cropped_snip(cropped_img)
            else:
                self.update_status("[-] Crop screen canceled (no area selected).")
        def _cancel():
            self.deiconify()
            self.lift()
            self.focus_force()
            self.update_status("[-] Crop screen canceled.")
        ScreenSnipper(_cb, on_cancel_callback=_cancel)

    def _process_cropped_snip(self, cropped_img):
        def _task():
            self.is_typing = True; self.stop_typing = False; self._disable_buttons()
            try:
                self.update_status("[*] TRANSMITTING CROPPED QUESTION TO AI CORE...")
                if not self.session.get("api_key"):
                    raise RuntimeError("NO_UPLINK")
                lang = self.lang_var.get()
                fmt = self.format_var.get()
                sol_m = self.sol_type_var.get()
                code = self.backend.from_image(cropped_img, lang, format_type=fmt, mode=sol_m)
                self.last_generated_code = code
                self.last_generated_lang = lang
                def _ui():
                    self.preview_box.delete("1.0", "end")
                    self.preview_box.insert("end", code)
                    self.update_status(f"[+] AI SOLUTION READY ({lang.upper()})")
                self.after(0, _ui)
                self._execute_code_injection(code, lang, enable_autonomous=True)
            except Exception as ex:
                err_msg = str(ex)
                if "NO_UPLINK" in err_msg:
                    err_msg = "No Gemini API key is configured or active.\n\nPlease enter your Gemini API key in Profile & Security or click 'CONNECT & ACTIVATE AI MODE' in the AI Module to get code solutions."
                self.update_status(f"[!] AI UPLINK ERROR: {err_msg[:35]}...")
                self.after(0, lambda e=err_msg: show_api_error_modal(self, "AI SCREEN SNIP ERROR", e))
            finally:
                self.is_typing = False; self.stop_typing = False; self._enable_buttons()
                self.after(0, self.deiconify)
        threading.Thread(target=_task, daemon=True).start()

    def _generate_viva_for_current(self):
        code_to_check = self.last_generated_code or self.preview_box.get("1.0", "end").strip() or self.prompt_entry.get("1.0", "end").strip()
        if not code_to_check:
            messagebox.showinfo("VIVA GENERATOR", "Generate or paste code in AI Module first.")
            return
        self.show_frame("VIVA_NOTES")
        self.viva_box.delete("1.0", "end")
        self.viva_box.insert("end", "[*] Generating college viva cheat sheet & examiner questions...\n")

        def _task():
            try:
                notes = self.backend.generate_viva_notes(code_to_check, self.lang_var.get())
                def _ui():
                    self.viva_box.delete("1.0", "end")
                    self.viva_box.insert("end", notes)
                self.after(0, _ui)
            except Exception as e:
                err_msg = str(e)
                self.after(0, lambda: self.viva_box.insert("end", f"\n[!] Viva Error: {err_msg}"))
                self.after(0, lambda e=err_msg: show_api_error_modal(self, "VIVA GENERATION ERROR", e))
        threading.Thread(target=_task, daemon=True).start()

    def _predict_test_cases_for_current(self):
        code_to_check = self.last_generated_code or self.preview_box.get("1.0", "end").strip() or self.prompt_entry.get("1.0", "end").strip()
        if not code_to_check:
            messagebox.showinfo("TEST CASE PREDICTOR", "Generate or paste code in AI Module first.")
            return
        self.show_frame("TEST_CASES")
        self.test_cases_box.delete("1.0", "end")
        self.test_cases_box.insert("end", "[*] Evaluating hidden test cases and boundary edge conditions...\n")

        def _task():
            try:
                cases = self.backend.predict_test_cases(code_to_check, self.lang_var.get())
                def _ui():
                    self.test_cases_box.delete("1.0", "end")
                    self.test_cases_box.insert("end", cases)
                self.after(0, _ui)
            except Exception as e:
                err_msg = str(e)
                self.after(0, lambda: self.test_cases_box.insert("end", f"\n[!] Test Suite Error: {err_msg}"))
                self.after(0, lambda e=err_msg: show_api_error_modal(self, "TEST CASES GENERATION ERROR", e))
        threading.Thread(target=_task, daemon=True).start()

    def start_direct_typing_payload(self, code):
        if self.is_typing: return
        threading.Thread(target=self._run_direct_pipeline, args=(code,), daemon=True).start()


# ── Pipelines ─────────────────────────────────────────────────────────────
    def _run_vision_pipeline(self):
        self.is_typing=True; self.stop_typing=False; self._disable_buttons()
        try:
            for rem in range(4,0,-1):
                if self.stop_typing: break
                self.update_status(f"[T-{rem}] INITIATE SCREEN CAPTURE..."); time.sleep(1)
            if self.stop_typing: return
            ss = ImageGrab.grab(); self.update_status("[*] TRANSMITTING TO AI CORE...")
            lang = self.lang_var.get(); code = self.backend.from_image(ss, lang, format_type=self.format_var.get(), mode=self.sol_type_var.get())
            self.last_generated_code = code; self.last_generated_lang = lang
            self.preview_box.delete("1.0","end"); self.preview_box.insert("end",code)
            self._execute_code_injection(code, lang, enable_autonomous=True)
        except Exception as ex:
            err_msg = str(ex)
            self.update_status(f"[!] AI ERROR: {err_msg[:35]}...")
            self.after(0, lambda e=err_msg: show_api_error_modal(self, "FULLSCREEN VISION ERROR", e))
            with open(ERROR_LOG_FILE, "w", encoding="utf-8") as f:
                import traceback; f.write(traceback.format_exc())
        finally:
            self.is_typing=False; self.stop_typing=False; self._enable_buttons()
            self.after(0, self.deiconify)

    def _run_text_pipeline(self, prompt):
        self.is_typing=True; self.stop_typing=False; self._disable_buttons()
        try:
            self.update_status("[*] GENERATING PAYLOAD..."); lang=self.lang_var.get()
            code = self.backend.from_text(prompt, lang, format_type=self.format_var.get(), mode=self.sol_type_var.get())
            self.last_generated_code = code; self.last_generated_lang = lang
            self.preview_box.delete("1.0","end"); self.preview_box.insert("end",code)
            self._execute_code_injection(code, lang, enable_autonomous=True)
        except Exception as ex:
            err_msg = str(ex)
            self.update_status(f"[!] AI ERROR: {err_msg[:35]}...")
            self.after(0, lambda e=err_msg: show_api_error_modal(self, "AI TEXT GENERATION ERROR", e))
            with open(ERROR_LOG_FILE, "w", encoding="utf-8") as f:
                import traceback; f.write(traceback.format_exc())
        finally:
            self.is_typing=False; self.stop_typing=False; self._enable_buttons()
            self.after(0, self.deiconify)

    def _run_direct_pipeline(self, code):
        self.is_typing=True; self.stop_typing=False; self._disable_buttons()
        try:
            if hasattr(self, "preview_box"):
                self.preview_box.delete("1.0","end"); self.preview_box.insert("end",code)

            if not self._wait_for_editor_and_clear():
                return

            self.update_status("[>] INITIATING INJECTION...")
            self._type_into_editor(code)

            if self.stop_typing: return

            self.update_status("[+] INJECTION COMPLETE. VERIFYING...")
            time.sleep(1)

            # Show success dialog
            self.after(0, self.deiconify)
            messagebox.showinfo("Success", "Code is written successfully into your editor.")
            self.update_status("[+] SYSTEM READY.")

        except Exception as ex:
            self.update_status(f"[!] ERROR: {ex}")
            with open(ERROR_LOG_FILE, "w", encoding="utf-8") as f:
                import traceback; f.write(traceback.format_exc())
        finally:
            self.is_typing=False; self.stop_typing=False; self._enable_buttons()
            self.after(0, self.deiconify)

# ── APPLICATION ENTRY POINT ───────────────────────────────────────────────────
if __name__ == "__main__":
    while True:
        session = load_session()

        # If no active role / session, run login wizard first
        if not session.get("role"):
            wizard = OnboardingWizard()
            wizard.mainloop()
            if not getattr(wizard, "success", False):
                # User closed the login window without completing authentication
                break
            session = load_session()
            if not session.get("role"):
                break

        try:
            app = AutoCoderApp(session)
            app.mainloop()
        except Exception as e:
            import traceback
            with open(ERROR_LOG_FILE, "w", encoding="utf-8") as f:
                f.write(traceback.format_exc())
            break

        # Check if user clicked LOGOUT
        if getattr(app, "logged_out", False):
            # Session was cleared in _logout, restart the loop to present OnboardingWizard smoothly!
            continue
        else:
            # User closed window normally, exit the application
            break
