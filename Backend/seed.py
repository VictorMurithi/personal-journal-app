from app import create_app, db
from models import User, Category, JournalEntry
from datetime import datetime

def seed_data():
    app = create_app()
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()

        # Create default categories
        categories = ['Personal', 'Work', 'Travel', 'Health', 'Finance']
        category_objs = []
        for category in categories:
            category_obj = Category(name=category)
            db.session.add(category_obj)
            category_objs.append(category_obj)
        db.session.commit()

        # Create default users
        users = [
            {'username': 'johndoe', 'password': 'password123'},
            {'username': 'janedoe', 'password': 'password456'},
            {'username': 'alice', 'password': 'alicepassword'},
            {'username': 'bob', 'password': 'bobpassword'},
            {'username': 'charlie', 'password': 'charliepassword'}
        ]
        user_objs = []
        for user_data in users:
            user = User(username=user_data['username'])
            user.set_password(user_data['password'])
            db.session.add(user)
            user_objs.append(user)
        db.session.commit()

        # Create journal entries for the users
        journal_entries = [
            {
                'title': 'My First Entry',
                'content': 'This is the content of my first journal entry.',
                'category': category_objs[0],
                'date': datetime.strptime('2023-07-01', '%Y-%m-%d'),
                'author': user_objs[0]
            },
            {
                'title': 'Work Progress',
                'content': 'Today I made significant progress on my work project.',
                'category': category_objs[1],
                'date': datetime.strptime('2023-07-02', '%Y-%m-%d'),
                'author': user_objs[1]
            },
            {
                'title': 'Vacation Plans',
                'content': 'I am planning a vacation to the mountains.',
                'category': category_objs[2],
                'date': datetime.strptime('2023-07-03', '%Y-%m-%d'),
                'author': user_objs[2]
            },
            {
                'title': 'Health Checkup',
                'content': 'I had my annual health checkup today.',
                'category': category_objs[3],
                'date': datetime.strptime('2023-07-04', '%Y-%m-%d'),
                'author': user_objs[3]
            },
            {
                'title': 'Financial Planning',
                'content': 'Started planning my finances for the next year.',
                'category': category_objs[4],
                'date': datetime.strptime('2023-07-05', '%Y-%m-%d'),
                'author': user_objs[4]
            },
            {
                'title': 'Second Entry',
                'content': 'This is the content of my second journal entry.',
                'category': category_objs[0],
                'date': datetime.strptime('2023-07-06', '%Y-%m-%d'),
                'author': user_objs[0]
            },
            {
                'title': 'Work Update',
                'content': 'Completed the project I was working on.',
                'category': category_objs[1],
                'date': datetime.strptime('2023-07-07', '%Y-%m-%d'),
                'author': user_objs[1]
            },
            {
                'title': 'Travel Plans',
                'content': 'Booked tickets for my trip.',
                'category': category_objs[2],
                'date': datetime.strptime('2023-07-08', '%Y-%m-%d'),
                'author': user_objs[2]
            },
            {
                'title': 'Fitness Routine',
                'content': 'Started a new fitness routine.',
                'category': category_objs[3],
                'date': datetime.strptime('2023-07-09', '%Y-%m-%d'),
                'author': user_objs[3]
            },
            {
                'title': 'Investment Ideas',
                'content': 'Explored some new investment ideas.',
                'category': category_objs[4],
                'date': datetime.strptime('2023-07-10', '%Y-%m-%d'),
                'author': user_objs[4]
            }
        ]

        for entry in journal_entries:
            journal_entry = JournalEntry(
                title=entry['title'],
                content=entry['content'],
                category=entry['category'],
                date=entry['date'],
                author=entry['author']
            )
            db.session.add(journal_entry)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
