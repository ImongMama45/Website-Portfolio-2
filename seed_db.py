import os
import django
from django.core.files import File
from pathlib import Path
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio_Website.settings')
django.setup()

from portfolio.models import Skill, Project, Profile, Education, Experience, Award, Certification
from django.conf import settings

BASE_DIR = settings.BASE_DIR

# Define the original static images path
static_images_dir = BASE_DIR / 'portfolio' / 'static' / 'portfolio' / 'images'

def get_image_file(filename):
    file_path = static_images_dir / filename
    if file_path.exists():
        return File(open(file_path, 'rb'), name=filename)
    return None

def seed_skills():
    print("Seeding Skills...")
    skills_data = [
        {"name": "HTML", "icon": "html.png", "order": 1},
        {"name": "CSS", "icon": "css.png", "order": 2},
        {"name": "JavaScript", "icon": "javascript-logo-javascript-icon-transparent-free-png.webp", "order": 3},
        {"name": "Responsive Web Design", "icon": "5339184.png", "order": 4},
        {"name": "Graphic Artist", "icon": "graphic.png", "order": 5},
    ]

    for data in skills_data:
        skill, created = Skill.objects.get_or_create(name=data['name'], defaults={'order': data['order']})
        if created or not skill.icon:
            img_file = get_image_file(data['icon'])
            if img_file:
                skill.icon.save(data['icon'], img_file)
                print(f"  Added Skill: {data['name']}")
            else:
                print(f"  [Warning] Missing image for skill: {data['name']}")
        else:
            print(f"  Skill already exists: {data['name']}")

def seed_projects():
    print("\nSeeding Projects...")
    projects_data = [
        {
            "title": "Lori and Gil's Website",
            "image": "lori-gil.png",
            "url_link": "https://github.com/ImongMama45",
            "order": 1,
            "role": "Frontend Developer",
            "tech_stack": "HTML, CSS, JavaScript",
            "description": "Designed and developed a responsive static website for local clients."
        },
        {
            "title": "Art Portfolio",
            "image": "Art.png",
            "url_link": "https://www.instagram.com/kabutogan69/",
            "order": 2,
            "role": "Illustrator / Designer",
            "tech_stack": "Procreate, Photoshop, Illustrator",
            "description": "A curated collection of my digital illustration and graphic design work."
        },
        {
            "title": "My Personal Website",
            "image": "enrollment.png",
            "url_link": "https://imongmama45.github.io/portfolio/",
            "order": 3,
            "role": "Full-Stack Developer",
            "tech_stack": "Django, HTML, CSS",
            "description": "My professional portfolio built to showcase my skills, projects, and creative work."
        },
    ]

    for data in projects_data:
        project, created = Project.objects.get_or_create(title=data['title'], defaults={
            'url_link': data['url_link'],
            'order': data['order'],
            'role': data['role'],
            'tech_stack': data['tech_stack'],
            'description': data['description']
        })
        if created or not project.image:
            img_file = get_image_file(data['image'])
            if img_file:
                project.image.save(data['image'], img_file)
                print(f"  Added Project: {data['title']}")
            else:
                print(f"  [Warning] Missing image for project: {data['title']}")
        else:
            print(f"  Project already exists: {data['title']}")

def seed_profile_data():
    print("\nSeeding Profile and Credentials...")
    
    # Singleton Profile
    profile, created = Profile.objects.get_or_create(name="Russell Alisan")
    if created:
        profile.bio = "A passionate developer and designer."
        profile.save()
        print("  Created Profile")
    else:
        print("  Profile already exists")

    # Sample Education
    edu, created = Education.objects.get_or_create(
        profile=profile,
        school_name="[SAMPLE] Sample University — Delete Me",
        defaults={
            'degree': 'B.S. Computer Science',
            'field_of_study': 'Software Engineering',
            'start_year': 2020,
            'end_year': 2024,
            'description': 'Sample description. Please delete this row from the admin panel.'
        }
    )
    if created: print("  Added Sample Education")

    # Sample Experience
    exp, created = Experience.objects.get_or_create(
        profile=profile,
        company_name="[SAMPLE] Acme Corp — Delete Me",
        defaults={
            'position': 'Junior Developer',
            'start_date': date(2024, 1, 1),
            'is_current': True,
            'description': 'Sample description. Please delete this row from the admin panel.'
        }
    )
    if created: print("  Added Sample Experience")

    # Sample Award
    award, created = Award.objects.get_or_create(
        profile=profile,
        award_name="[SAMPLE] Best Developer — Delete Me",
        defaults={
            'organization': 'Tech Community',
            'award_year': 2023,
            'description': 'Sample description. Please delete this row from the admin panel.'
        }
    )
    if created: print("  Added Sample Award")

    # Sample Certification
    cert, created = Certification.objects.get_or_create(
        profile=profile,
        certification_name="[SAMPLE] AWS Certified — Delete Me",
        defaults={
            'issuing_organization': 'Amazon Web Services',
            'issue_date': date(2023, 5, 15),
            'description': 'Sample description. Please delete this row from the admin panel.'
        }
    )
    if created: print("  Added Sample Certification")

if __name__ == '__main__':
    seed_skills()
    seed_projects()
    seed_profile_data()
    print("\nDatabase seeding complete!")
