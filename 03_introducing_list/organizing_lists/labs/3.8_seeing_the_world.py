# 1. Store locations in non-alphabetical order
locations = ['delhi', 'mumbai', 'kolkata', 'chennai', 'bangalore']

# 2. Print original order
print("Original order:", locations)

# 3. Print alphabetically using sorted() without modifying list
print("Alphabetical order (sorted):", sorted(locations))

# 4. Show original order is preserved
print("Original order preserved:", locations)

# 5. Print in reverse alphabetical order using sorted(reverse=True)
print("Reverse alphabetical (sorted):", sorted(locations, reverse=True))

# 6. Show original order is preserved
print("Original order preserved:", locations)

# 7. Change list order permanently using reverse()
locations.reverse()
print("Reversed order:", locations)

# 8. Restore original order using reverse()
locations.reverse()
print("Restored original order:", locations)

# 9. Sort list in alphabetical order permanently using sort()
locations.sort()
print("Permanent alphabetical order:", locations)

# 10. Sort list in reverse alphabetical order permanently using sort(reverse=True)
locations.sort(reverse=True)
print("Permanent reverse alphabetical order:", locations)
