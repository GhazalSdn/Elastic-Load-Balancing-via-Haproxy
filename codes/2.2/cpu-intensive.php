<?php
echo "CPU intensive request <br>";
$a = 1.0001;
$n = 1000000;
$f = 1;
for($i = 1; $i < ($n + 1); $i++){
  $f = $f * $a;
}
echo "$a to the power of $n = $f <br>";
?>
