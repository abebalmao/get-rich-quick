Getting connection to url... \n
<?php
	$baseUrl = 'https://eu.api.blizzard.com/data/wow/auctions/commodities?namespace=dynamic-eu&access_token=';
	$token = 'USjxuNR6LQDBKhoPxtbOBrYh01jbHWfazI';
	$url = $baseUrl . $token;

	$outputFile = dirname(dirname(getcwd())) . 'util\output.txt';//C:\xampp\htdocs\git\get-rich-quick\output.txt';

	$handle = fopen($url, 'r');
	$fileHandle = fopen($outputFile, 'w');

	// Read the file in chunks and write each chunk to the file
	while (!feof($handle)) {
	    $chunk = fread($handle, 8192); // Read 8KB at a time
	    
	    // Write the chunk to the file
	    fwrite($fileHandle, $chunk);
	}

	// Close the file handles
	fclose($handle);
	fclose($fileHandle);

	echo 'Done!';

	/*
	$handle = fopen($url, 'r');

	// Read the file in chunks
	while (!feof($handle)) {
	    echo fread($handle, 8192); // Read 8KB at a time
	}

	// Close the file handle
	fclose($handle);
	*/



