def computeShippingPrice(height, width, depth, weight):
    return 5 * height * width * depth + 0.5 * weight

if __name__ == "__main__":
    x = computeShippingPrice(10, 10, 10, 10)
    print("Compute shippingPrice:", x)