(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? lst) 'YOUR-CODE-HERE
    (cond 
        ((null? lst) #t)
        ((null? (cdr lst)) #t)
        (else 
              (if (> (car lst) (car (cdr lst)))
                #f
                (ascending? (cdr lst))))))

(define (interleave lst1 lst2) 'YOUR-CODE-HERE
  (cond ((and (null? lst1) (null? lst2)) nil)                
        ((null? lst1) (interleave lst2 lst1))                  
        (else (cons (car lst1) (interleave lst2 (cdr lst1))))) 
) 

(define (my-filter func lst) 'YOUR-CODE-HERE
  (cond ((null? lst) nil)  
        ((func (car lst))
           (cons (car lst) (my-filter func (cdr lst))))
        (else (my-filter func (cdr lst)))))

(define (no-repeats lst) 'YOUR-CODE-HERE
  (cond ((null? lst) nil)
        (else (cons (car lst) 
                    (no-repeats
                       (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst)))))))