(function() {
         
    // store the slider in a local variable
    var $window = $(window),
    flexslider;
    
    // tiny helper function to add breakpoints
    function getGridSize() {
    return (window.innerWidth < 280) ? 1 :
    (window.innerWidth < 600) ? 2 :
    (window.innerWidth < 800) ? 2 :
    (window.innerWidth < 900) ? 2 : 5;
    }
    
    $window.load(function() {
    
        // Carouse2						
     $('#flexCarouse2').flexslider({
            animation: "slide",
            animationLoop: false,
            itemWidth: 380,
            itemMargin: 25,
            minItems: 1,
            maxItems: 1,
            //slideshow: 1,
            move: 1,
            pausePlay: true,
            pauseText: 'Pause',
            playText: 'Play', 
            controlNav: false,
            start: function(slider){
              $('body').removeClass('loading');
              if (slider.pagingCount === 1) slider.addClass('flex-centered');
            }
          });
    
    });
    
    }());    
    
    
    
$(window).load(function(){
// Slider						
    $('#flexSlider').flexslider({
        animation: "slide",
        pausePlay: true,
        controlNav: true,
        start: function(slider){
        $('body').removeClass('loading');
        }
    });
    $('#flexSlider1').flexslider({
        animation: "slide",
        controlNav: false,
        start: function(slider){
        $('body').removeClass('loading');
        }
    });
    $('#flexSlider2').flexslider({
        animation: "slide",
        controlNav: false,
        start: function(slider){
        $('body').removeClass('loading');
        }
    });    
    
    $('#contSlider1').flexslider({
        animation: "swing",
        controlNav: false,
        directionNav: false,
        direction: "vertical",
        easing:'linear',
        prevText: " ",
        nextText: " ", 
        minItems: 2,
        maxItems: 2,
        move: 2,
        itemMargin: 0,
        pausePlay: true,
        pauseOnHover: true,
        slideshowSpeed:1000,
        animationSpeed:10000,      
        
    });
    
    $('#contSlider2').flexslider({
        animation: "slide",
        controlNav: false,
        start: function(slider){
        $('body').removeClass('loading');
        }
    });   
    
    
// Carousel						
    $('#flexCarousel').flexslider({
        animation: "slide",
        animationLoop: false,
        itemWidth: 200,
        itemMargin: 5,
        minItems: 2,
        maxItems: 6,
        slideshow: 1,
        move: 1,
        pausePlay: true,
        pauseText: 'Pause',
        playText: 'Play', 
        controlNav: false,
        start: function(slider){
            $('body').removeClass('loading');
            if (slider.pagingCount === 1) slider.addClass('flex-centered');
        }
        });
    
    
    // Carouse2						
    /*$('#flexCarouse2').flexslider({
        animation: "slide",
        animationLoop: false,
        itemWidth: 320,
        itemMargin: 5,
        minItems: 2,
        maxItems: 3,
        slideshow: 1,
        move: 1,
        pausePlay: true,
        pauseText: 'Pause',
        playText: 'Play', 
        controlNav: false,
        start: function(slider){
            $('body').removeClass('loading');
            if (slider.pagingCount === 1) slider.addClass('flex-centered');
        }
        });*/
    
    
    
    $('#flexCarousel1').flexslider({
        animation: "slide",
        animationLoop: false,
        itemWidth: 168,
        itemMargin: 20,
        minItems:1,
        maxItems: 4,
        slideshow: 1,
        move: 1,
        controlNav: false,
        start: function(slider){
            $('body').removeClass('loading');
            //if (slider.pagingCount === 1) slider.addClass('flex-centered');
        }
        });
    // breaking_news

    $('#breaking_news').flexslider({
    animation: "slide",
    controlNav: false,
    animationLoop: true,
    directionNav: false,
    direction: "horizontal",
    slideshowSpeed: 7000,
    animationSpeed: 600,
        initDelay: 1000,
        pausePlay: true,
    pauseText: '',
    playText: '',
    pauseOnHover: false
    });

    // Gallery
        $('#galleryCarousel').flexslider({
        animation: "fade",
        controlNav: "thumbnails",
        start: function(slider){
            $('body').removeClass('loading');
        }
        });
    });

$(document).ready(function(){
    $('figure img').ma5gallery({
        preload:true
    });
    
    $('#socialTab').easyResponsiveTabs({
            type: 'default', //Types: default, vertical, accordion
            width: 'auto', //auto or any width like 600px
            fit: true, // 100% fit in a container
            tabidentify: 'socialTab_1', // The tab groups identifier
            activate: function(event) { // Callback function if tab is switched
                var $tab = $(this);
                var $info = $('#nested-tabInfo');
                var $name = $('span', $info);
                $name.text($tab.text());
                $info.show();
            }
        });
    
    $('#feedTab').easyResponsiveTabs({
            type: 'default', //Types: default, vertical, accordion
            width: 'auto', //auto or any width like 600px
            fit: true, // 100% fit in a container
            tabidentify: 'feedTab_1', // The tab groups identifier
            activate: function(event) { // Callback function if tab is switched
                var $tab = $(this);
                var $info = $('#nested-tabInfo');
                var $name = $('span', $info);
                $name.text($tab.text());
                $info.show();
            }
        });
    
    $('.resp-tabs-list li a').click(function(event){
                event.preventDefault();								 
            })

});
    
    var a = 0;
    $(window).scroll(function() {
    
      var oTop = $('#counter').offset().top - window.innerHeight;
      if (a == 0 && $(window).scrollTop() > oTop) {
        $('.count').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });
        a = 1;
      }
    
    });

$(document).ready(function(){
    $('figure img').ma5gallery({
        preload:true
    });
});
    
$(document).ready(function() {
    //Horizontal Tab
    $('#parentHorizontalTab').easyResponsiveTabs({
        type: 'default', //Types: default, vertical, accordion
        width: 'auto', //auto or any width like 600px
        fit: true, // 100% fit in a container
        tabidentify: 'hor_1', // The tab groups identifier
        activate: function(event) { // Callback function if tab is switched
            var $tab = $(this);
            var $info = $('#nested-tabInfo');
            var $name = $('span', $info);
            $name.text($tab.text());
            $info.show();
        }
    });

    // Child Tab
    $('#ChildVerticalTab_1').easyResponsiveTabs({
        type: 'vertical',
        width: 'auto',
        fit: true,
        tabidentify: 'ver_1', // The tab groups identifier
        activetab_bg: '#fff', // background color for active tabs in this group
        inactive_bg: '#fff', // background color for inactive tabs in this group
        active_border_color: '#c1c1c1', // border color for active tabs heads in this group
        active_content_border_color: '#5AB1D0' // border color for active tabs contect in this group so that it matches the tab head border
    });


        var videoPlayButton,
        videoWrapper = document.getElementsByClassName('video-wrapper')[0],
        video = document.getElementsByTagName('video')[0],
        videoMethods = {
            renderVideoPlayButton: function() {
                    if (videoWrapper.contains(video)) {
                    this.formatVideoPlayButton()
                    video.classList.add('has-media-controls-hidden')
                    videoPlayButton = document.getElementsByClassName('video-overlay-play-button')[0]
                    videoPlayButton.addEventListener('click', this.hideVideoPlayButton)
                    }
            },
            formatVideoPlayButton: function() {
                    videoWrapper.insertAdjacentHTML('beforeend', '\
                    <svg class="video-overlay-play-button" viewBox="0 0 200 200" alt="Play video">\
                        <circle cx="100" cy="100" r="90" fill="none" stroke-width="15" stroke="#fff"/>\
                        <polygon points="70, 55 70, 145 145, 100" fill="#fff"/>\
                    </svg>\
                    ')
            },
            hideVideoPlayButton: function() {
                    video.play()
                    videoPlayButton.classList.add('is-hidden')
                    video.classList.remove('has-media-controls-hidden')
                    video.setAttribute('controls', 'controls')
            }
        }
        videoMethods.renderVideoPlayButton()
});

// ====Tab scrolling text====
function changeClass(){    
    var x = document.getElementsByClassName("text-slide"); 
    var y = document.getElementsByClassName("scroll-text");                           
    x[0].classList.toggle ("pause");
    y[0].classList.toggle("scroll-left");                            
}
function changeClass1(){    
    var x = document.getElementsByClassName("text-slide1"); 
    var z = document.getElementsByClassName("scroll-text-1");                              
    x[0].classList.toggle ("pause");
    z[0].classList.toggle("scroll-left");                             
}

// ===== Scroll to Top ==== 
$(document).ready(function(){ 
    $(document).scroll(function() { 
        if ($(this).scrollTop() > 100) { 
            $('#scroll').fadeIn(); 
        } else { 
            $('#scroll').fadeOut(); 
        } 
    }); 
    $('#scroll').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 800); 
        return false; 
    }); 
 });
