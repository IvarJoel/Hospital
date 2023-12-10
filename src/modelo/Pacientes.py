from modelo.Coneccion import conexion2023
from flask import jsonify, request

def buscar_paci(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM pacientes WHERE ci = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()

        if datos != None:
            paci = {'cedula_identidad': datos[0], 'nombre': datos[1],
                       'apell_pat': datos[2], 'apell_mat': datos[3],
                       'direccion': datos[4]}
            return paci
        else:
            return None
    except Exception as ex:
            raise ex
    

class ModeloPaciente():
    @classmethod
    def listar_Paciente(self):
        try:
            conn = conexion2023()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM pacientes")
            datos = cursor.fetchall()
            pacientes = []

            for fila in datos:
                paci = {'cedula_identidad': fila[0],
                       'nombre': fila[1],
                       'apell_pat': fila[2],
                       'apell_mat': fila[3],
                       'direccion': fila[4]}
                pacientes.append(paci)

            conn.close()

            return jsonify({'pacientes': pacientes, 'mensaje': "pacientes listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})
    
    @classmethod
    def lista_Paciente(self,codigo):
        try:
            usuario = buscar_paci(codigo)
            if usuario != None:
                return jsonify({'usuarios': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def registrar_paciente(self):
        try:
            usuario = buscar_paci(request.json['ci_e'])
            if usuario != None:
                return jsonify({'mensaje': "Cedula de identidad  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT INTO pacientes values(%s,%s,%s,%s,%s)', (request.json['ci_e'], request.json['nombre_e'], request.json['apell_pat_e'],
                                                                            request.json['apell_mat_e'], request.json['direccion_e']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    
    @classmethod
    def actualizar_paciente(self,codigo):
        try:
            usuario = buscar_paci(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE pacientes SET nombre=%s, apell_pat=%s, apell_mat=%s,
                direccion=%s WHERE ci=%s""",
                        (request.json['nombre_e'], request.json['apell_pat_e'], request.json['apell_mat_e'], request.json['direccion_e'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "paciente actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "paciente  no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def eliminar_paciente(self,codigo):
        try:
            usuario = buscar_paci(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM pacientes WHERE ci = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "paciente eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "paciente no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})