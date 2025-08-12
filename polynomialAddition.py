class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

def insert_term(head, coeff, power):
    new_node = Node(coeff, power)
    if not head or head.power < power:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.power > power:
        current = current.next
    if current.next and current.next.power == power:
        current.next.coeff += coeff
        return head
    new_node.next = current.next
    current.next = new_node
    return head

def input_polynomial():
    head = None
    n = int(input("Enter number of terms: "))
    for _ in range(n):
        coeff, power = map(int, input("Enter coefficient and power: ").split())
        head = insert_term(head, coeff, power)
    return head

def print_polynomial(head):
    terms = []
    while head:
        terms.append(f"{head.coeff}x^{head.power}")
        head = head.next
    print(" + ".join(terms))

def add_polynomials(poly1, poly2):
    result = None
    while poly1 or poly2:
        if not poly1:
            result = insert_term(result, poly2.coeff, poly2.power)
            poly2 = poly2.next
        elif not poly2:
            result = insert_term(result, poly1.coeff, poly1.power)
            poly1 = poly1.next
        elif poly1.power > poly2.power:
            result = insert_term(result, poly1.coeff, poly1.power)
            poly1 = poly1.next
        elif poly1.power < poly2.power:
            result = insert_term(result, poly2.coeff, poly2.power)
            poly2 = poly2.next
        else:
            result = insert_term(result, poly1.coeff + poly2.coeff, poly1.power)
            poly1 = poly1.next
            poly2 = poly2.next
    return result

# Input polynomials
print("Enter first polynomial:")
poly1 = input_polynomial()
print("Enter second polynomial:")
poly2 = input_polynomial()

# Add polynomials
result = add_polynomials(poly1, poly2)

# Output result
print("Resultant polynomial:")
print_polynomial(result)
