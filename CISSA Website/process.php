<?php
echo "Hello World!";
if($_POST['formSubmit'] == "Submit Request")
{
	echo "Hello World!";
	$errorMessage = "";
	
	if(empty($_POST['username']))
	{
		$errorMessage .= "<li>Username is empty </li>";
	}
	if(empty($_POST['email']))
	{
		$errorMessage .= "<li>Email is empty </li>";
	}
		if(empty($_POST['org']))
	{
		$errorMessage .= "<li>Organization is empty </li>";
	}
	$varusername = $_POST['username'];
	$varemail = $_POST['email'];
	$varorg = $_POST['org'];

	if(empty($errorMessage)) 
	{
		$fs = fopen("mydata.csv","a");

		print_r(error_get_last());
		fwrite($fs,$varusername . ", " . $varemail . ", " .$varorg "\n");
		fclose($fs);

		header("Location: thankyou.html");
		exit;
	}
}
?>
