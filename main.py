import pandas as pd

# ===============================
# Load datasets
# ===============================
courses = pd.read_csv("data/courses_clean_with_domain.csv")
internships = pd.read_csv("data/internships_cleaned.csv")

# ===============================
# Normalize user input
# ===============================
user_input = input("Enter your interest: ").strip().lower()

# ===============================
# Keyword mapping (SHORT + FULL)
# ===============================
domain_keywords = {
    "ai": ["ai", "artificial intelligence", "machine learning", "ml", "deep learning", "nlp"],
    "data": ["data", "data science", "data analyst", "analytics", "big data"],
    "web": ["web", "web development", "frontend", "backend", "full stack"],
    "cloud": ["cloud", "aws", "azure", "gcp", "devops"]
}

# ===============================
# Detect domain automatically
# ===============================
detected_domain = None
for domain, keywords in domain_keywords.items():
    for word in keywords:
        if word in user_input:
            detected_domain = domain.upper()
            break
    if detected_domain:
        break

if not detected_domain:
    print("\n❌ No matching domain found. Try AI / Data / Web / Cloud")
    exit()

print("\n🎓 Student Guidance System")
print(f"\n📚 Recommended Courses for {detected_domain}:\n")

# ===============================
# FILTER COURSES
# ===============================
course_matches = courses[
    courses["domain"].str.upper() == detected_domain
].head(10)

if course_matches.empty:
    print("No courses found.")
else:
    for _, row in course_matches.iterrows():
        print(f"🔹 {row.get('title')}")
        print(f"   ⏱ Duration : {row.get('duration')}")
        print(f"   🌐 Language : {row.get('language')}")
        print(f"   🔗 URL      : {row.get('url')}")
        print("-" * 60)

# ===============================
# FILTER INTERNSHIPS
# ===============================
print(f"\n💼 Recommended Internships for {detected_domain}:\n")

internship_matches = internships[
    internships["domain"].str.upper() == detected_domain
].head(10)

if internship_matches.empty:
    print("No internships found.")
else:
    for _, row in internship_matches.iterrows():
        print(f"🔹 {row['Job Title']}")
        print(f"   📍 Location : {row['Location']}")
        print(f"   🎯 Level    : {row['Experience']}")
        print(f"   🛠 Skills   : {row['Skills']}")
        print("-" * 60)

print("\n✅ Guidance complete!")
