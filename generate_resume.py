import yaml
import os
import sys

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)["roles"]

def update_latex_config(job_role, config):
    with open("config.tex", "w") as file:
        file.write(f"\\newcommand{{\\JobTitle}}{{{config['job_title']}}}\n")
        file.write(f"\\newcommand{{\\SkillOne}}{{{config.get('skill_one', 'Skill 1')}}}\n")
        file.write(f"\\newcommand{{\\SkillTwo}}{{{config.get('skill_two', 'Skill 2')}}}\n")
        file.write(f"\\newcommand{{\\SkillThree}}{{{config.get('skill_three', 'Skill 3')}}}\n")
        file.write(f"\\newcommand{{\\SkillFour}}{{{config.get('skill_four', 'Skill 4')}}}\n")
        file.write(f"\\newcommand{{\\ProjectOneTitle}}{{{config.get('project_one_title', 'Project 1')}}}\n")
        file.write(f"\\newcommand{{\\ProjectOneDesc}}{{{config.get('project_one_desc', 'Description 1')}}}\n")

def main():
    config = load_config()
    job_role = sys.argv[1] if len(sys.argv) > 1 else "Machine Learning Engineer"
    
    if job_role not in config:
        print("Invalid job role! Exiting.")
        sys.exit(1)

    print(f"✅ Updating resume for {job_role}...")
    update_latex_config(job_role, config[job_role])

if __name__ == "__main__":
    main()
