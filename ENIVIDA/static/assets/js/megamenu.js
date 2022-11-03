// JavaScript Document For The mega Menu
  
$(".main-menu").accessibleMegaMenu({
	/* prefix for generated unique id attributes, which are required 
		to indicate aria-owns, aria-controls and aria-labelledby */
	uuidPrefix: "accessible-megamenu",

	/* css class used to define the megamenu styling */
	menuClass: "nav-menu",

	/* css class for a top-level navigation item in the megamenu */
	topNavItemClass: "nav-item",

	/* css class for a megamenu panel */
	panelClass: "sub-nav",

	/* css class for a group of items within a megamenu panel */
	panelGroupClass: "sub-nav-group",

	/* css class for the hover state */
	hoverClass: "hover",

	/* css class for the focus state */
	focusClass: "focus",

	/* css class for the open state */
	openClass: "open"
});
		  
$(document).ready(function(e) {	 
	
	$('.main-menu li').each(function(index, element) {
		if($(this).children('div').length > 0){
			$(this).find('> a').append('<span class="indicator">+</span>');
			
			$(this).children('a').click(function(e) {
				e.preventDefault();
			});		
		}		
	});

	$('#main_menu .nav-item>a').mouseleave(function(e) {
		if($(this).parent().children('div').length > 0){
		
		}else{
			
			$(this).blur();
		}
	});

	// de focus when mouse leave, it was geting stucked
	$('#main_menu .nav-item').mouseleave(function(e) {
		$(this).children('a').blur();
	})

	// on focus open dropdown for norml element
	$('#main_menu .nav-item a').focus(function(e) {	
		if($(this).parent().children('div').length > 0){
			if($(document).innerWidth() > 940){
				$(this).click();
			}
		}	
	});
	
	// On focus open dropdown for appended element
	$(document).on('focus', '#overflow_menu .nav-item a', function () {
	if($(this).parent().children('div').length > 0){
				if($(document).innerWidth() > 940){
					$(this).click();
				}
	}
	//alert(1);
	});
	
	// On focus open dropdown script for the more button
	/*$(document).on('focus', '#btn-more-toggle', function () {
	$(this).click();
	
	});*/

});
		  
function menu_toggle(){		
	//$('.megamenu-wraper .container .showhide').css('display', 'block');
	//$('.megamenu-wraper .container').prepend('');	
	$('.showhide').click(function(e) {
		$('#main_menu').stop().slideToggle('slow');
		$('.showhide').toggleClass('close');
		
	});
	
	
	/*$(document).on('click', '.indicator', function(){ 
		//$(this).parent('a').next('div').stop().slideToggle('slow');
		alert(1);
		
	});*/ 
	if($(document).innerWidth() < 940){
		$('.main-menu .nav-item a').click(function(e) {
			$(this).next('div').stop().slideToggle('slow');
		});		
	}
}
		  
$(window).resize(function(e){
	if($(document).innerWidth() > 940){
			
		$('.main-menu .nav-item').each(function(index, element) {
			$(this).children('a').removeClass('sub-nav');
		})
			$('#main_menu').show();
			$('#main_menu').attr('style','');
		
		//$('.megamenu-wraper .container .showhide').css('display', 'none');
		
	}else{
		//$('.megamenu-wraper .container .showhide').css('display', 'block');
		
	}
	//alert(1);
		
})
		  
window.onload =  menu_toggle(); 
		  
$(document).ready(function(e) {
	//alert($('.carousel-wrapper').innerWidth());
	if($(document).innerWidth()>940){
		var t = $('#main_menu').width();
		var m = 0;
		$('#main_menu .nav-menu .nav-item').each(function(index, element) {
			m = m + $(this).width();
			if(m>(t-100)){
			$('#btn-more-toggle').parent().remove();
			$(this).parent().append('<li class="btn-more-li"><a class="btn-more" id="btn-more-toggle" href="#"><span>More</span></a></li>');
				
				$(this).remove();
				$('#overflow_menu ul.nav-menu').append('<li class="nav-item">'+$(this).html()+'</li>');
			}
		});
	}else{
		$('.main-menu .sub-nav').slideUp();
		$('.main-menu').slideUp();
	}
	  
	  
	$('#overflow_menu').hide();
	var oh = $('#btn-more-toggle').height();
	$('#btn-more-toggle').mousedown(function(e) {
		mousedown = true;
		//debugger;
		//console.log($('#overflow_menu ul').height() + $('#main_menu').height());
		e.preventDefault();
		$('#overflow_menu').stop().slideToggle(500);
		var mHight = $('#main_menu ul li').first().height();
		$(this).toggleClass('opened');
		if($(this).hasClass('opened')){
			var t = $('#overflow_menu ul').height() + $('#main_menu').height()+3;
			$(this).stop().animate({height: t+'px'},500);
		}else{
			$(this).stop().animate({height: mHight+'px'},500);
		}
	});
	$('#btn-more-toggle').focus(function(e) {
		//debugger;
		//console.log($('#overflow_menu ul').height() + $('#main_menu').height());
		e.preventDefault();
		$('#overflow_menu').stop().slideToggle(500);
		var mHight = $('#main_menu ul li').first().height();
		$(this).toggleClass('opened');
		if($(this).hasClass('opened')){
			var t = $('#overflow_menu ul').height() + $('#main_menu').height()+3;
			$(this).stop().animate({height: t+'px'},500);
		}else{
			$(this).stop().animate({height: mHight+'px'},500);
		}
	});
});