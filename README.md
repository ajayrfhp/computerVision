# computerVision
### Currently available scripts.
* Sudoku Solver
* Harris Corner Detector
* Irregular Shape Detection
* Hough Transform
* Prototype License Plate Detection
* Contour
* PCA
* Convolution, can be extended to edge detection. (Sobel Filter). Speed of convolution to be improved.
* Edge Filter implemented by convolving image with the mask. To be extended for color edges.


###EXAMPLE 
* Sudoku Solver

 ![Original Image for Sudoku Solver ]( pictures/sudoku.jpg "Input SUdoku")
 * Adaptive Thresholding 
 ![Threshold ]( output/threshold.png "After Thresholding")
 * Detect Contour with biggest area
 ![Sudoku region detection ]( output/sudokudetected.png "Sudoku region detection")
 * Perspective Transform
 ![Perspective Transform ]( output/perspectivetransform.png "Perspective Transform")
 ![One Grid ]( output/sub_sudoku.png "One Grid")
 ![One Digit Raw ]( output/raw_digit.png "One Digit Raw")
 * FloodFill in the boundaries
 ![Floodilled Digit ]( output/digit_floodfill.png "FloodFilled Digit")
 * Eroded and Scaled
 ![Digit ]( output/digit.png "Digit")

* Harris Corner Detector
  
 ![Original Image]( pictures/chess_board.png "Original ChessBoard")
 ![Corners Detected]( output/simple_harris_corner.png "Corners Detected")

* Edge Detection

 ![Original Image ]( pictures/depay.jpg "RGB Image")
 ![Edge detection ]( pictures/depaynew.png "Edge detected")
 





### Resources
* [SudoKu Solver](http://aishack.in/tutorials/sudoku-grabber-opencv-plot/)
* [Edge Detection](http://blog.saush.com/2011/04/20/edge-detection-with-the-sobel-operator-in-ruby/) 
* [Computer Vision Cook Book](http://programmingcomputervision.com/)

