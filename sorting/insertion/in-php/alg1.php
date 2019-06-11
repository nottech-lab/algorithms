<?php
    //Part 1 : Implementation of the algorithm
    function  sortData($ar) {
        $size = count($ar);
        for ($j = 2; $j <= $size; $j++){
            $num = $ar[$j - 1];
            for($i = $j - 2; $i >= 0; $i--){
                if($ar[$i] > $ar[$i+1]){
                    $ar[$i+1] = $ar[$i];
                    $ar[$i] = $num;
                }
            }
        }
        return $ar;
    }

    //Part 2: Testing the algorithm
    //NOTE: This part is not part of the algorithm
    $random_numbers = range(0, 100);
    shuffle($random_numbers);
    $unsorted = array_slice($random_numbers ,0,10);
    echo implode(" ",$unsorted) . "\n";
    $sorted = sortData($unsorted);
    echo implode(" ",$sorted) . "\n";