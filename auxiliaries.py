def image_string( image, divider="," ):
    '''this function will take as input a 2D array referred to by image and return 
    a string version of this 2D array that is separated by tabs'''
    imageString = ""
    count = 1
    for row in image: 
        for col in row:
            imageString = imageString + str(col)
            if count % len(row) == 0:
                imageString = imageString + "\n"
            else:
                imageString = imageString + divider
            count = count + 1
    return imageString
