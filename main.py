from dll import Doublelinkedlist


if __name__ == "__main__":
    via = Doublelinkedlist() 

    print("--- Estado Inicial (Vacío) ---")
    print(via)
    print("-" * 30)

   
    via.generate_random_vehicles(10)
    print("--- Después de generar vehículos ---")
    print(via)
    print("-" * 30)

    
    print("--- Requerimiento 1: Insertar vehículo 'FIN123' al final ---")
    via.append({'placa': 'FIN123', 'tipo': 'auto', 'prioridad': 3})
    print(via)
    print("-" * 30)

    
    print("--- Requerimiento 2: Dar paso preferencial (motos P1 al frente) ---")
    via.dar_paso_preferencial()
    print(via)
    print("-" * 30)

   
    print("--- Requerimiento 3: Eliminar camiones P > 3 ---")
    via.eliminar_camiones_inspeccion()
    print(via)
    print("-" * 30)

 
    if not via.find_node_by_plate("V003"):
        via.append({'placa': 'V003', 'tipo': 'auto', 'prioridad': 2})
    if not via.find_node_by_plate("V007"):
         via.append({'placa': 'V007', 'tipo': 'moto', 'prioridad': 4})
    print(f"--- Requerimiento 4: Simular accidente entre V003 y V007 (Eliminar intermedios) ---")
    print("Estado ANTES del accidente:")
    print(via)
    via.simular_accidente("V003", "V007")
    print("\nEstado DESPUÉS del accidente:")
    print(via)
    print("-" * 30)

 
    print("--- Requerimiento 5: Intentar invertir vía si más autos que motos ---")
    via.invertir_via_si_mas_autos()
    print(via)
    print("-" * 30)

  
    print("--- Requerimiento 6: Reorganizar por prioridad (sin estructuras auxiliares) ---")
    via.reorganizar_por_prioridad()
    print(via)
    print("-" * 30)

    print("--- EJECUCIÓN FINALIZADA ---")
