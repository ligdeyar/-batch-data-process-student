from classes.DbMongo import DbMongo
from classes.data import *
import pymongo

class Dataprocess:

    def __init__(self, data):
        self.__data = data
        self.__collection = "estudiantes"

    def create_careers(self):
        ## Do something to create careers on your mongodb collection using __data
        #lo que hace es leer la Lista DATA y cuando encuentre
        #la palabra carrera la guarde en un arreglo careers
    
        careers = []
        for career in self.__data:
           if "carrera" in career:
                careers.append(career["carrera"])
        return careers
                
     
    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        
        courses = []
        for courses in self.__data:
            cursos_reprobados = self.__data('cursos_reprobados')
            cursos_aprobados = self.__data('cursos_aprobados')
            if "cursos_reprobados" and 'cursos_aprobados' in cursos:
                courses_option = '{cursos_aprobados} at {cursos_reprobados}'
                courses.append(courses_option)
        return  courses
                

    def create_students(self):
        ## Do something to create students on your mongodb collection using __data

        students = []
        for nombre_completo in self.__data:
            if "nombre_completo" in nombre_completo:
                students_option = nombre_completo["nombre_completo"]
                students.append(students_option)
        return students

    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data

        enrollments = []
        for numero_cuenta in self.__data:
            if "numero_cuenta" in numero_cuenta:
                enrollments_option = numero_cuenta["numero_cuenta"]
                enrollments.append(enrollments_option)
        return enrollments

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        base = {'__id': self.__id}
        campos = {'$set': self.__dict__}
        collection.update_one(base,campos)
        client.close()

    def delete(self, db):
        collection = db[self.__collection]
        base = {'__id': self.__id}
        collection.delete_one(base)
        
    @staticmethod
    def get_one(db):
        collection = db["estudiantes"]
        base = { 'numero_cuenta' : numero_cuenta }
        result = collection.find_one(base)
        return Categoria( result["nombre_completo"] , result["numero_cuenta"] )

    @staticmethod
    def get_list(db):
        collection = db["estudiantes"]
        estudiantes = collection.find()

        list_estudiantes = []
        for e in estudiantes:
            temp_estudiantes = estudiantes(
                e["numero_cuenta"],
                e["nombre_completo"]
            )

            list_estudiantesa.append(temp_estudiantes)
        return list_estudiantes

    @staticmethod
    def delete_all(db):
        lista_e = Dataprocess.get(self, data)
        for e in lista_e:
            e.delete(db)

    