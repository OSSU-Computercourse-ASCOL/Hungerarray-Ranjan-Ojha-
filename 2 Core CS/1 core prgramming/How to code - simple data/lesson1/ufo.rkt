;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ufo) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

;screen dimension
(define WIDTH 900)
(define HEIGHT 720)
; background
(define grndheight (* HEIGHT 0.1))
(define bckgrnd (place-image(rectangle
                             WIDTH grndheight "solid" "black")
                            (/ WIDTH 2) HEIGHT
                            (empty-scene WIDTH HEIGHT "blue")))

; UFO
(define UFO (overlay (circle (+ (* WIDTH .02) (* HEIGHT .02))
                             "solid"
                             "green")
                     (rectangle (+ (* WIDTH 0.1) (* HEIGHT .1))
                                (+ (* WIDTH .01) (* HEIGHT .01))
                                "solid"
                                "green")))

(define mid
    (- HEIGHT (/ (image-height UFO ) 2)))
(define speed 2)


(define lim (- mid (/ grndheight 2)))
(define (land time)
  (cond
    [(<= (* time speed) lim)
     (place-image UFO (/ WIDTH 2) (* time speed) bckgrnd)]
    [(> (* time speed) lim)
     (place-image UFO (/ WIDTH 2) lim bckgrnd)]))

(animate land)
  
