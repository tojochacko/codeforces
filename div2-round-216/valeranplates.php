<?php
$stdin = fopen('php://stdin', 'r');
$i = 1;
$wash_counter = 0;

while($i <= 2) {
	$line = trim(fgets($stdin));
	$temp_arr = explode(' ', $line);
	if($i == 1) {
		$n = $temp_arr[0];
		$m = $temp_arr[1];
		$k = $temp_arr[2];
	}
	if($i == 2) {
		$dish_arr = $temp_arr;
	}
	$i++;
}

fclose($stdin);
//echo $n."\n";
//echo $m."\n";
//echo $k."\n";

//print_r($dish_arr);
for($j=0;$j<$n;$j++) {
	switch($dish_arr[$j]) {
		case 1:
			if($m != 0) {
				$m--;
			}
			else {
				$wash_counter++;
			}
			break;
		case 2:
			if($k != 0) {
				$k--;
				break;
			}
			if($m != 0) {
				$m--;
				break;
			}
			
			$wash_counter++;
			break;
	}
}

echo $wash_counter."\n";
?>
