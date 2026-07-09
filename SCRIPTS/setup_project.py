from pathlib import Path

# Root project folder
ROOT = Path(r"C:\Development\TITAN")

folders = [
    "PLAYBOOK",
    "SOFTWARE",
    "HARDWARE",
    "AI",
    "ELECTRONICS",
    "CAD",
    "RESEARCH",
    "DOCUMENTATION",
    "TESTING",
    "JOURNAL",
    "SCRIPTS",
    "TOOLS",
    "TEMP",
]

playbook_files = [
    "00_Master_Index.md",
    "01_Project_Charter.md",
    "02_Vision_and_Mission.md",
    "03_Engineering_Principles.md",
    "04_Project_Roadmap.md",
    "05_Development_Environment.md",
    "06_Folder_Structure.md",
    "07_Git_Workflow.md",
    "08_Coding_Standards.md",
    "09_Documentation_Standards.md",
    "10_New_PC_Setup.md",
    "CHANGELOG.md",
]

# Create folders
for folder in folders:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

# Create playbook files
for file in playbook_files:
    (ROOT / "PLAYBOOK" / file).touch(exist_ok=True)

# Create README.md
(ROOT / "README.md").touch(exist_ok=True)

print("✅ Project TITAN structure created successfully.")