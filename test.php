<?php

class Users
{
  $first_name = "karim";
  $last_name = "alaa";
  $birth_date = 1995;
  $age = 2016 - 1995;
  function get_user_data($first_name,$last_name,$age)
  {
    $full_name = $first_name + $last_name;
    print 'name  '.$full_name.'age  '.$age;
    return $full_name;
  }
}

class Mail
{
  $message = "hi";

  function print_subject()
  {
   print 'subject is hello';
  }

  function mail($message)
  {
   mail($message);
   print 'message sent successful';
   return true;
  }
}

$users = new Users();
$first_name = "Karim";
$last_name = "Alaa";
$age = 20;

$my_name = $first_name->get_user_data($first_name,$last_name,$age);
$mail = new Mail();
$mail_sent = $mail->mail();
print $my_name;

?>

