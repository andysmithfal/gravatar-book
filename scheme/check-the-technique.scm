; (repeat 5
(weave-forward 1)
(rotate-forward 2 3 8 9 10 15 16)
(weave-back 1)
(weave-forward 1)
(rotate-forward 6 7 11 12)
(repeat 2
  (rotate-forward 2 3 15 16))
(weave-back 1)
(rotate-back 6 7 8 9 10 11 12)
(weave-forward 1)
(rotate-forward 6 7 11 12)
(weave-back 1)
(rotate-back 2 3 4 5 8 9 10 13 14 15 16)
(rotate-back 4 5 8 9 10 13 14 15)
(weave-forward 1)
(repeat 2
(rotate-forward 8 9 10))
(weave-back 1)
(repeat 2
(rotate-back 8 9 10))
(weave-forward 1)
(repeat 2
(rotate-forward 2 3 4 5 13 14 15 16))
(weave-back 1)
(repeat 2
(rotate-forward 6 7 8 9 10 11 12))
(repeat 4
(rotate-forward 0 1 2 3 4 5 13 14 15 16 17 18))
(weave-forward 1)
;)