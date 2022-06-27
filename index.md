<!DOCTYPE html>
<!--[if lte 8]><html class="pre-ie9" lang="en"><![endif]-->
<!--[if gte IE 9]><!--><html lang="en"><!--<![endif]-->
<head>
  <title>Hello, world!</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="description" content="" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="style.css" />
  <link rel="icon" href="img/favicon.png">
  <meta name="theme-color" content="">
  <meta property="og:title" content="" />
  <meta property="og:description" content="" />
  <meta property="og:image" content="" />
  <meta name="twitter:card" content="">
  <meta name="twitter:site" content="">
  <meta name="twitter:title" content="">
  <meta name="twitter:description" content="">
  <meta name="twitter:image" content="">
</head>
<body>
  <div id="cookie-notice" class="w-100 bg-dark text-white pt-3 px-4 pb-1 position-fixed" style="z-index: 1000; bottom: 0;">
    <div class="container p-2">
      <div class="row">
        <div class="col-sm-8 col-md-9">
          <p class="p-2">This website uses cookies so that we can provide you with the best website experience. By clicking “I Accept” you acknowledge the use of cookies and to our <a href="#"><u>Privacy Policy</u></a>.</p> 
        </div>
        <div class="col-sm-4 col-md-3">
          <a class="i-accept btn btn-primary m-2">I Accept</a>
        </div>
      </div>
    </div>
  </div>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>
  <script type="text/javascript">
    (function($){
      $('.i-accept').on('click', function() {   
        if(localStorage.noshow !== '1') {
          $('#cookie-notice').addClass('d-none');
           localStorage.noshow='1';
        }  
      });
      if(localStorage.noshow == '1') {
        $('#cookie-notice').addClass('d-none');
      };
    })(jQuery);
  </script>
</body>
</html>
