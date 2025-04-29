import random
from node import node


class Doublelinkedlist:

  def __init__(self):
    self._head = None
    self._tail = None
    self.size = 0

  @property
  def head(self):
    return self._head

  @head.setter
  def head(self, Node):
    if Node is not None and not isinstance(Node, node):
      raise TypeError("head must be a Node or None")
    self._head = Node

  @property
  def tail(self):
    return self._tail

  @tail.setter
  def tail(self, Node):
    if Node is not None and not isinstance(Node, node):
      raise TypeError("tail must be a Node or None")
    self._tail = Node

  def __len__(self):
    return self.size

  def is_empty(self):
      return self.size == 0

  def __iter__(self):
    curnode = self.head
    while curnode is not None:
      yield curnode
      curnode = curnode.next

  def __str__(self):
    result = [str(node) for node in self]
    return ' <--> '.join(result) if result else "Vía Vacía"


  def prepend(self,value):
    newnode = node(value)
    if self.is_empty():
      self.head = newnode
      self.tail = newnode
    else:
      newnode.next = self.head
      self.head.prev = newnode
      self.head = newnode
    self.size += 1

  def append(self,value):
    newnode = node(value)
    if self.is_empty():
      self.head = newnode
      self.tail = newnode
    else:
      self.tail.next = newnode
      newnode.prev = self.tail
      self.tail = newnode
    self.size += 1

  def _remove_node(self, node_to_remove):
    if node_to_remove is None:
        return None

    prev_node = node_to_remove.prev
    next_node = node_to_remove.next

    if prev_node is not None:
        prev_node.next = next_node
    else: # Eliminando la cabeza
        self.head = next_node

    if next_node is not None:
        next_node.prev = prev_node
    else: # Eliminando la cola
        self.tail = prev_node

    node_to_remove.prev = None
    node_to_remove.next = None
    self.size -= 1
    return node_to_remove

  def popfirst(self):
    if self.is_empty():
        return None
    return self._remove_node(self.head)

  def pop(self):
    if self.is_empty():
        return None
    return self._remove_node(self.tail)

  def find_node_by_plate(self, placa):
      for current_node in self:
          if current_node.value['placa'] == placa:
              return current_node
      return None

 

  def dar_paso_preferencial(self):
      current_node = self.head
  
      while current_node is not None:
          next_node = current_node.next  
  
          if current_node.value['tipo'] == 'moto' and current_node.value['prioridad'] == 1:
              
              vehiculo = current_node.value
              self._remove_node(current_node)
              self.prepend(vehiculo)  # Lo ponemos al frente
          current_node = next_node


  def eliminar_camiones_inspeccion(self): 
      
      current_node = self.head
      while current_node is not None:
          next_node_to_check = current_node.next
          if current_node.value['tipo'] == 'camion' and current_node.value['prioridad'] > 3:
              self._remove_node(current_node)
          current_node = next_node_to_check

  def simular_accidente(self, placa1, placa2): 
      node1 = self.find_node_by_plate(placa1)
      node2 = self.find_node_by_plate(placa2)

      if not node1 or not node2:
          print(f"Error: No se encontró una o ambas placas ({placa1}, {placa2})")
          return

     
      start_node, end_node = None, None
      temp = self.head
      order_found = False
      while temp:
          if temp == node1:
              start_node = node1
              end_node = node2
              order_found = True
              break
          if temp == node2:
              start_node = node2
              end_node = node1
              order_found = True
              break
          temp = temp.next

      if not order_found:
          print("Error al determinar el orden de los nodos para el accidente.")
          return

   
      current = start_node.next
      while current and current != end_node:
          next_to_process = current.next
          self._remove_node(current)
          current = next_to_process


  def invertir_via_si_mas_autos(self): 
      count_autos = 0
      count_motos = 0
      for node in self:
          if node.value['tipo'] == 'auto':
              count_autos += 1
          elif node.value['tipo'] == 'moto':
              count_motos += 1

      if count_autos > count_motos:
          print("Invirtiendo vía (más autos que motos)...")
          current = self.head
          prev_node = None
          self.tail = self.head

          while current:
              next_node = current.next
              current.next = prev_node
              current.prev = next_node
              
              prev_node = current
              current = next_node

         
          self.head = prev_node
      else:
          print("No se invierte la vía (no hay más autos que motos).")


  def reorganizar_por_prioridad(self): 
      
      if self.is_empty() or self.size == 1:
          return # Ya está ordenada

      sorted_marker = self.head 
      current_node = self.head.next 

      while current_node is not None:
          next_to_consider = current_node.next # Guardamos el siguiente antes de mover current_node

         
          if current_node.value['prioridad'] >= sorted_marker.value['prioridad']:
              sorted_marker = current_node
          else:
              
              prev_c = current_node.prev
              next_c = current_node.next 

              prev_c.next = next_c
              if next_c is not None:
                  next_c.prev = prev_c
              else: 
                  self.tail = prev_c

              current_node.prev = None
              current_node.next = None
              
              insertion_point = self.head
              while insertion_point != next_to_consider and insertion_point.value['prioridad'] <= current_node.value['prioridad']:
                 insertion_point = insertion_point.next

             
              if insertion_point is None: 
                 prev_c.next = current_node
                 current_node.prev = prev_c
               
                 if next_c is None:
                    self.tail = current_node
                 
                 else:
                     current_node.next = next_c
                     next_c.prev = current_node


              elif insertion_point.prev is None: 
                  current_node.next = self.head
                  self.head.prev = current_node
                  self.head = current_node
              else: 
                  prev_insertion = insertion_point.prev
                  prev_insertion.next = current_node
                  current_node.prev = prev_insertion
                  current_node.next = insertion_point
                  insertion_point.prev = current_node

              

          
          current_node = next_to_consider

 
  def generate_random_vehicles(self, num_vehicles):
     
      tipos = ['auto', 'moto', 'camion']
      for i in range(num_vehicles):
          placa = f"V{i+1:03d}"
          tipo = random.choice(tipos)
          prioridad = random.randint(1, 5)
          self.append({'placa': placa, 'tipo': tipo, 'prioridad': prioridad})
