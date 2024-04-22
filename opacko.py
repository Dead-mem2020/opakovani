import statistics
cisla = [3, 5, 8, 1, 2, 4, 6, 7]

print("Tohle je z 1. úkolu: ")

cisla.sort()
print(cisla)
print()

cisla.sort(reverse=True)
print(cisla)

print()
print(statistics.mean([3, 5, 8, 1, 2, 4, 6, 7]))
print()