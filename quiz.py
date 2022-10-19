class LanguageStudent:
    def __init__(self, languages):
        self.languages = languages

    def languages(self):
        language_list = [self.languages]
        return language_list

    def add_language(self, language):
        language_list_new = languages(self).append(language)
        return language_list_new

    pass

class LanguageTeacher(LanguageStudent):
    def __init__(self, languages, student):
        self.languages = languages
        self.student = student

    def teach(self, student, language):
        if student.languages() != self.language and teacher.languages() == self.language:
            student.addlanguages(self.language)

    pass

teacher = LanguageTeacher()
teacher.add_language('English')
student = LanguageStudent()
teacher.teach(student, 'English')
print(student.languages)