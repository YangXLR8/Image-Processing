import cv2
import math
import numpy as np

# Grayscale an image
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Divide an image into horizontal strips
def divide_horizontally(image, num_strips):
    height = image.shape[0]
    strip_height = math.ceil(height / num_strips)  # height is rounded to integer
    strips = []
    for i in range(num_strips):
        start_y = i * strip_height
        end_y = min((i + 1) * strip_height, height)
        strips.append(image[start_y:end_y, :])
    return strips

# Divide an image into vertical strips
def divide_vertically(image, num_strips):
    width = image.shape[1]
    strip_width = math.ceil(width / num_strips)
    strips =[]
    for i in range(num_strips):
        start_x = i * strip_width
        end_x = min((i + 1) * strip_width, width)
        strips.append(image[:, start_x:end_x])
    return strips

# Assemble strips into horizontal or vertical images
def assemble_strips(strips, is_horizontal=True):
    if is_horizontal:
        axis = 0
        assembled_horizontal_image1 = np.concatenate([strips[i] for i in range(len(strips)) if i % 2 == 0], axis)
        assembled_horizontal_image2 = np.concatenate([strips[i] for i in range(len(strips)) if i % 2 != 0], axis)
        return assembled_horizontal_image1, assembled_horizontal_image2
    else:
        axis = 1
        assembled_vertical_image1 = np.concatenate([strips[i] for i in range(len(strips)) if i % 2 == 0], axis)
        assembled_vertical_image2 = np.concatenate([strips[i] for i in range(len(strips)) if i % 2 != 0], axis)
        return assembled_vertical_image1, assembled_vertical_image2
    

def main():
    num_strips = int(input("Enter the number of strips: "))

    image = cv2.imread('TestImage.jpg')
    image = cv2.resize(image, (500, 500))
    gray_image = grayscale(image)
    strips = divide_horizontally(gray_image, num_strips)
    horiz_left_image, horiz_right_image = assemble_strips(strips, is_horizontal=True)

    first_merge = np.concatenate((horiz_left_image,  horiz_right_image), axis=1)
    
    # Save the images
    cv2.imwrite('out/horiz_left_image.jpg',  horiz_left_image)
    cv2.imwrite('out/horiz_right_image.jpg',  horiz_right_image)
    cv2.imwrite('out/first_merged_image.jpg', first_merge)



    strips = divide_vertically(first_merge, num_strips)
    ver_left_image, ver_right_image = assemble_strips(strips, is_horizontal=False)

    final_merge = np.concatenate((ver_left_image, ver_right_image), axis=0)
    
    
    cv2.imwrite('out/vertical_left_image.jpg', ver_left_image)
    cv2.imwrite('out/vertical_right_image.jpg', ver_right_image)
   
    cv2.imwrite('out/final.jpg', final_merge)   
    cv2.imshow("final_merge", final_merge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()