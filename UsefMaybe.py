import numpy as np
import cv2
import math

#Making an rgb class that works like a vector namespace in unity C#
class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self, other):
        return RGB(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return RGB(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self, scalar):
        return RGB(self.r * scalar, self.g * scalar, self.b *scalar)

    def __str__(self):
        return f"{self.r}, {self.g}, {self.b}"

#Contains Image paths of the compare images
images = ["C:/users/13173/Downloads/im2.jpg"]

#RGB List
rgb = []

#The current image
current_image = 0

#Color Dictionary
colors = {"Red": 0,"Orange": 0,"Yellow": 0,"Green":0,"Blue": 0,"Purple": 0,"Black": 0,"Brown": 0,"White": 0, "Gray": 0}

#Resolution
#Placehold value, change later
res = 360000

#The two images we need to compare
compare_image = cv2.imread(images[current_image])

c = 1

theString = "c:/users/13173/Downloads/im" + str(c) + ".jpg"

material_image = cv2.imread(theString)

#Finally, the actual comparison (After pushing the dictionary to a list)
compare_image_list = []
material_image_list = []

feature_vector = []

#Loops to the next image to compare to
def LoopToNextImage():
    global current_image
    global compare_image
    current_image += 1
    compare_image = cv2.imread(images[current_image])

#The color image comparison
def ColorComparison():
    row = 0
    coloumn = 0
    euDis = []
    compare_colors = {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0, "Blue": 0, "Purple": 0, "Brown": 0, "White": 0, "Black": 0, "Gray": 0}
    for x in range(res):
        euDis = []
        pixel = material_image[row, coloumn]
        pixelValue = RGB(pixel[2], pixel[1], pixel[0])
        rgb.append(pixelValue)
        if coloumn != 639:
            coloumn += 1
        elif coloumn == 639:
            row += 1
            coloumn = 0
        #print("stuck1")
        distanceRed = math.sqrt((255 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceOrange = math.sqrt((255 - pixelValue.r)**2 + (165 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceYellow = math.sqrt((255 - pixelValue.r)**2 + (255 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceGreen = math.sqrt((0 - pixelValue.r)**2 + (128 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceBlue = math.sqrt((0 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (255 - pixelValue.b)**2)
        distancePurple = math.sqrt((128 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (128 - pixelValue.b)**2)
        distanceBlack = math.sqrt((0 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceBrown = math.sqrt((139 - pixelValue.r)**2 + (69 - pixelValue.g)**2 + (19 - pixelValue.b)**2)
        distanceWhite = math.sqrt((255 - pixelValue.r)**2 + (255 - pixelValue.g)**2 + (255 - pixelValue.b)**2)
        distanceGray = math.sqrt((128 - pixelValue.r)**2 + (128 - pixelValue.g)**2 + (128 - pixelValue.b)**2)
        euDis.append(distanceRed)
        euDis.append(distanceOrange)
        euDis.append(distanceYellow)
        euDis.append(distanceGreen)
        euDis.append(distanceBlue)
        euDis.append(distancePurple)
        euDis.append(distanceBlack)
        euDis.append(distanceBrown)
        euDis.append(distanceWhite)
        euDis.append(distanceGray)
        #print("stuck2")
        
        if min(euDis) == distanceRed:
            colors["Red"] += 1
        elif min(euDis) == distanceOrange:
            colors["Orange"] += 1
        elif min(euDis) == distanceYellow:
            colors["Yellow"] += 1
        elif min(euDis) == distanceGreen:
            colors["Green"] += 1
        elif min(euDis) == distanceBlue:
            colors["Blue"] += 1
        elif min(euDis) == distancePurple:
            colors["Purple"] += 1
        elif min(euDis) == distanceBlack:
            colors["Black"] += 1
        elif min(euDis) == distanceBrown:
            colors["Brown"] += 1
        elif min(euDis) == distanceWhite:
            colors["White"] += 1
        elif min(euDis) == distanceGray:
            colors["Gray"] += 1
        #print("stuck3")
    material_image_list.append(colors["Red"])
    material_image_list.append(colors["Orange"])
    material_image_list.append(colors["Yellow"])
    material_image_list.append(colors["Green"])
    material_image_list.append(colors["Blue"])
    material_image_list.append(colors["Purple"])
    material_image_list.append(colors["Brown"])
    material_image_list.append(colors["Black"])
    material_image_list.append(colors["White"])
    material_image_list.append(colors["Gray"])
    row = 0
    coloumn = 0
    for x in range(res):
        euDis = []
        pixel = compare_image[row, coloumn]
        pixelValue = RGB(pixel[2], pixel[1], pixel[0])
        rgb.append(pixelValue)
        if coloumn != 639:
            coloumn += 1
        elif coloumn == 639:
            row += 1
            coloumn = 0
        #print("stuck1")
        distanceRed = math.sqrt((255 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceOrange = math.sqrt((255 - pixelValue.r)**2 + (165 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceYellow = math.sqrt((255 - pixelValue.r)**2 + (255 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceGreen = math.sqrt((0 - pixelValue.r)**2 + (128 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceBlue = math.sqrt((0 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (255 - pixelValue.b)**2)
        distancePurple = math.sqrt((128 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (128 - pixelValue.b)**2)
        distanceBlack = math.sqrt((0 - pixelValue.r)**2 + (0 - pixelValue.g)**2 + (0 - pixelValue.b)**2)
        distanceBrown = math.sqrt((139 - pixelValue.r)**2 + (69 - pixelValue.g)**2 + (19 - pixelValue.b)**2)
        distanceWhite = math.sqrt((255 - pixelValue.r)**2 + (255 - pixelValue.g)**2 + (255 - pixelValue.b)**2)
        distanceGray = math.sqrt((128 - pixelValue.r)**2 + (128 - pixelValue.g)**2 + (128 - pixelValue.b)**2)
        euDis.append(distanceRed)
        euDis.append(distanceOrange)
        euDis.append(distanceYellow)
        euDis.append(distanceGreen)
        euDis.append(distanceBlue)
        euDis.append(distancePurple)
        euDis.append(distanceBlack)
        euDis.append(distanceBrown)
        euDis.append(distanceWhite)
        euDis.append(distanceGray)
        #print("stuck2")
        
        if min(euDis) == distanceRed:
            compare_colors["Red"] += 1
        elif min(euDis) == distanceOrange:
            compare_colors["Orange"] += 1
        elif min(euDis) == distanceYellow:
            compare_colors["Yellow"] += 1
        elif min(euDis) == distanceGreen:
            compare_colors["Green"] += 1
        elif min(euDis) == distanceBlue:
            compare_colors["Blue"] += 1
        elif min(euDis) == distancePurple:
            compare_colors["Purple"] += 1
        elif min(euDis) == distanceBlack:
            compare_colors["Black"] += 1
        elif min(euDis) == distanceBrown:
            compare_colors["Brown"] += 1
        elif min(euDis) == distanceWhite:
            compare_colors["White"] += 1
        elif min(euDis) == distanceGray:
            compare_colors["Gray"] += 1
        #print("stuck3")
    compare_image_list.append(compare_colors["Red"])
    compare_image_list.append(compare_colors["Orange"])
    compare_image_list.append(compare_colors["Yellow"])
    compare_image_list.append(compare_colors["Green"])
    compare_image_list.append(compare_colors["Blue"])
    compare_image_list.append(compare_colors["Purple"])
    compare_image_list.append(compare_colors["Brown"])
    compare_image_list.append(compare_colors["Black"])
    compare_image_list.append(compare_colors["White"])
    compare_image_list.append(compare_colors["Gray"])
    
    #Now the Euclidean Distance
    final_color_distance = math.sqrt((compare_image_list[0] - material_image_list[0])**2 + (compare_image_list[1] - material_image_list[1])**2 + (compare_image_list[2] - material_image_list[2])**2 + (compare_image_list[3] - material_image_list[3])**2 + (compare_image_list[4] - material_image_list[4])**2 + (compare_image_list[5] - material_image_list[5])**2 + (compare_image_list[6] - material_image_list[6])**2 + (compare_image_list[7] - material_image_list[7])**2 + (compare_image_list[8] - material_image_list[8])**2 + (compare_image_list[9] - material_image_list[9])**2)
    feature_vector.append(final_color_distance)




def LBP():
    row = 0
    coloumn = 0
    all_binary_patterns = {}
    for x in range(res):
        
        rowcoloumn = []
        
        binary_pattern = "0"
        
        material_intensity = material_image[row, coloumn][0]
        if(material_image[row+1, coloumn][0] >= material_intensity):
            binary_pattern = "1"
        if(material_image[row+1, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(material_image[row, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(material_image[row-1, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(material_image[row-1, coloumn][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(material_image[row-1, coloumn-1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(material_image[row, coloumn-1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(material_image[row+1, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        
        if binary_pattern in all_binary_patterns:
            all_binary_patterns[binary_pattern] += 1
        else:
            all_binary_patterns.__setitem__(binary_pattern, 1)
        
        
        rowcoloumn = [row, coloumn]
        
        
        if(coloumn < 597):
            coloumn += 1
        else:
            coloumn = 0
            row += 1
    # Calculate total pattern occurrences
    total_patterns = sum(all_binary_patterns.values())

    # Calculate normalized frequencies
    normalized_frequencies = {pattern: freq / total_patterns for pattern, freq in all_binary_patterns.items()}

    # Calculate entropy
    entropy = -sum(p * math.log2(p) for p in normalized_frequencies.values() if p > 0)
    
    row = 0
    coloumn = 0
    
    for x in range(res):
        
        rowcoloumn = []
        
        binary_pattern = "0"
        
        material_intensity = compare_image[row, coloumn][0]
        if(compare_image[row+1, coloumn][0] >= material_intensity):
            binary_pattern = "1"
        if(compare_image[row+1, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(compare_image[row, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(compare_image[row-1, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(compare_image[row-1, coloumn][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(compare_image[row-1, coloumn-1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(compare_image[row, coloumn-1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        if(compare_image[row+1, coloumn+1][0] >= material_intensity):
            binary_pattern += "1"
        else:
            binary_pattern += "0"
        
        if binary_pattern in all_binary_patterns:
            all_binary_patterns[binary_pattern] += 1
        else:
            all_binary_patterns.__setitem__(binary_pattern, 1)
        
        rowcoloumn = [row, coloumn]
        
        if(coloumn < 597):
            coloumn += 1
        else:
            coloumn = 0
            row += 1
            
    # Calculate total pattern occurrences
    total_patterns = sum(all_binary_patterns.values())

    # Calculate normalized frequencies
    normalized_frequencies = {pattern: freq / total_patterns for pattern, freq in all_binary_patterns.items()}

    # Calculate entropy
    compare_entropy = -sum(p * math.log2(p) for p in normalized_frequencies.values() if p > 0)
    dis = math.sqrt((entropy-compare_entropy)**2)
    feature_vector.append(dis)





def ImageFreq():
    material_grayscale = cv2.cvtColor(material_image, cv2.COLOR_BGR2GRAY)
    compare_grayscale = cv2.cvtColor(compare_image, cv2.COLOR_BGR2GRAY)
    
    min_height = min(material_grayscale.shape[0], compare_grayscale.shape[0])
    min_width = min(material_grayscale.shape[1], compare_grayscale.shape[1])

    material_grayscale = material_grayscale[:min_height, :min_width]
    compare_grayscale = compare_grayscale[:min_height, :min_width]

    
    material_fft = np.fft.fft2(material_grayscale)
    compare_fft = np.fft.fft2(compare_grayscale)
    
    material_shifted = np.fft.fftshift(material_fft)
    compare_shifted = np.fft.fftshift(compare_fft)
    magnitude_spectrum1 = np.abs(material_shifted)
    magnitude_spectrum2 = np.abs(compare_shifted)
    mse = np.mean((magnitude_spectrum1 - magnitude_spectrum2)**2)
    feature_vector.append(mse)


while True:
    for x in range(len(images)):
        ColorComparison()
        LBP()
        ImageFreq()
        print("Color Comparison: " + str(feature_vector[0]) + " Entropy: " + str(feature_vector[1]) + " FFT:" + str(feature_vector[2]))
        threshold = [20000, 0.4, 40000000]
        amount = 0
        if threshold[0] > feature_vector[0]:
            amount+=1
        if(threshold[1]>feature_vector[1]):
            amount+=1
        if(threshold[2]>feature_vector[2]):
            amount+=1
        if(amount>=2):
            print("accurate")
        else:
            print("not accurate")
        if x != len(images) - 1:
            LoopToNextImage()
    c = c + 1
    theString = "C:/users/13173/Downloads/im" + str(c) + ".jpg"
    