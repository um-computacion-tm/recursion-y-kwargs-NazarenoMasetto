import unittest 

def buscar_datos(*args, **kwargs):
    args_set = set(args)

    for key, value in kwargs.items():
        values_set = set(value.values())
        
        if args_set == values_set:
            return key
    
    return None


database = {
    "persona1": {
        "primer_nombre": "Nazareno",
        "segundo_nombre": "Jose",
        "primer_apellido": "Masetto",
        "segundo_apellido": "Nahman"
    },
    "persona2": {
        "primer_nombre": "Michael",
        "primer_apellido": "Jordan"
    },
    "persona3": {
        "primer_nombre": "Gonzalo",
        "primer_apellido": "Martinez",
        "segundo_apellido": "Perez"
    },
    "persona4": {
        "primer_nombre": "Antonella",
        "segundo_nombre": "Sol",
        "primer_apellido": "Bonelli",
        "segundo_apellido": "Oriolo"
    },
    "persona5": {
        "primer_nombre": "Cristian",
        "segundo_nombre": " Gabriel",
        "primer_apellido": "Romero"
    }  
}      


class TestBuscarDatos(unittest.TestCase):
    def test_buscar_datos_persona1(self):
        result = buscar_datos("Nazareno", "Jose", "Masetto", "Nahman", **database)
        self.assertEqual(result, "persona1")

    def test_buscar_datos_persona2(self):
        result = buscar_datos("Michael", "Jordan", **database)
        self.assertEqual(result, "persona2")
        
    def test_buscar_datos_persona3(self):
       result = buscar_datos("Gonzalo", "Martinez", "Perez", **database)
       self.assertEqual(result, "persona3") 
       
    def test_buscar_datos_persona4(self):
       result = buscar_datos("Antonella", "Sol", "Bonelli", "Oriolo", **database)
       self.assertEqual(result, "persona4") 
       
    def test_buscar_datos_persona5(self):
       result = buscar_datos("Cristian", "Gabriel", "Romero", **database)
       self.assertEqual(result, "persona5")
         
    def test_buscar_datos_no_encontrado(self):
        result = buscar_datos("Pedro", "Sanchez", **database)
        self.assertIsNone(result, None)
            

    
unittest.main()