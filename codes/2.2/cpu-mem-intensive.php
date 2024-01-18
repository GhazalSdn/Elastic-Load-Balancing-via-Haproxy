<?php
echo "CPU and Memory intensive request <br>";
$arr = [];
$n = 1000000;
$a = 1.0001;

$arr[0] = $a;
for ($i = 1; $i < $n; $i++)
{
$arr[$i] = $arr[$i-1] * $a;
}
echo "Array is created <br>";
echo "For example: arr[99999] = $arr[99999]<br>";
?>