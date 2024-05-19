import cadquery as cq

def create_box_with_hole(length, width, height, hole_diameter):
    """
    Функція для створення коробки з отвором.
    
    Args:
        length (float): Довжина коробки.
        width (float): Ширина коробки.
        height (float): Висота коробки.
        hole_diameter (float): Діаметр отвору.
        
    Returns:
        cq.Workplane: Результат операцій CadQuery.
    """
    # Створення коробки
    box = cq.Workplane("XY").box(length, width, height)
    
    # Створення отвору
    hole = box.faces(">Z").workplane().hole(hole_diameter)
    
    return hole

if __name__ == '__main__':
    # Параметри коробки та отвору
    box_length = 90
    box_width = 50
    box_height = 20
    hole_diameter = 10
    
    # Створення об'єкту з отвором
    result = create_box_with_hole(box_length, box_width, box_height, hole_diameter)
    
    # Показати об'єкт
    show_object(result)
