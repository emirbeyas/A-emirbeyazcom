import datetime
import firebase_admin
from firebase_admin import credentials,firestore


class webContent:
    homeTitle = ""
    homeDegree = ""
    homeDescription = ""
    homeImgUrl = ""
    qualificationEducation = []
    qualificationWork = []
    skills = []
    skillsLength = 0
    portfolioList = []
    portfolioLength = 0
    discord = ""
    email = ""
    location = ""
    github = ""
    instagram = ""
    linkedin = ""
    cvlink = ""
    
    credentialData = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(credentialData)
    firestoreDb = firestore.client()
    
    def __init__(self):
        self.homeTitle = self.firestoreDb.collection('HOME').document('CONTENT').get().to_dict().get('TITLE')
        self.homeDegree = self.firestoreDb.collection('HOME').document('CONTENT').get().to_dict().get('DEGREE')
        self.homeDescription = self.firestoreDb.collection('HOME').document('CONTENT').get().to_dict().get('DESCRIPTION')
        self.homeImgUrl = self.firestoreDb.collection('HOME').document('CONTENT').get().to_dict().get('IMAGEURL')
        self.qualificationEducation = self.firestoreDb.collection('QUALIFICATION').document('EDUCATION').get().to_dict().get('QUALIFICATION')
        self.qualificationWork = self.firestoreDb.collection('QUALIFICATION').document('WORK').get().to_dict().get('QUALIFICATION')
        
        col = self.firestoreDb.collection('SKILLS').get()
        for i in col:
            lst = []
            lst.append(i.id)
            for j in i.to_dict().get('SKILL'):
                lst.append(j)
            self.skills.append(lst)
        self.skillsLength = len(col)

        col2 = list(self.firestoreDb.collection('PORTFOLIO').get())
        for i in col2:
            lst = []
            lst.append(i.to_dict().get('TITLE'))
            lst.append(i.to_dict().get('IMGURL'))
            lst.append(i.to_dict().get('DESCRIPTION'))
            lst.append(i.to_dict().get('GITHUBURL'))
            self.portfolioList.append(lst)

        self.portfolioLength = len(col2)

        self.discord = self.firestoreDb.collection('CONTACTME').document('CONTACTME').get().to_dict().get('DISCORD')
        self.email = self.firestoreDb.collection('CONTACTME').document('CONTACTME').get().to_dict().get('EMAIL')
        self.location = self.firestoreDb.collection('CONTACTME').document('CONTACTME').get().to_dict().get('LOCATION')
        self.github = self.firestoreDb.collection('CONTACTME').document('CONTACTME').get().to_dict().get('GITHUB')
        self.instagram = self.firestoreDb.collection('CONTACTME').document('CONTACTME').get().to_dict().get('INSTAGRAM')
        self.linkedin = self.firestoreDb.collection('CONTACTME').document('CONTACTME').get().to_dict().get('LINKEDIN')
        self.cvlink = self.firestoreDb.collection('CONTACTME').document('CONTACTME').get().to_dict().get('CVLINK')

    def sendMessage(self, senderName, senderMail, senderSubject, senderMessage):
        now = datetime.datetime.now()
        self.firestoreDb.collection('MESSAGES').document(str(now)).set(
            {
            'senderName': str(senderName),
            'senderMail': str(senderMail),
            'senderSubject': str(senderSubject),
            'senderMessage': str(senderMessage)
            }
        )
