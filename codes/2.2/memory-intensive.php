<?php
echo "Memory intensive request <br>";
$arr = [];
$n = 1000000;
for ($i = 0; $i < $n; $i++)
{
  $arr[$i] = $i;
}
echo "Array is created <br>";
echo "for example: arr[25] = $arr[25]";
?>
