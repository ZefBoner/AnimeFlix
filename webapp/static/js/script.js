document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navbarLinks = document.querySelector('.navbar-links');
  
    menuToggle.addEventListener('click', function() {
      navbarLinks.classList.toggle('active');
    });
  });

  window.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const login = document.querySelector('.login');
  
    const handleResize = () => {
      if (window.innerWidth <= 768) {
        sidebar.style.display = 'none';
        login.style.display = 'none';
      } else {
        sidebar.style.display = 'block';
        login.style.display = 'flex';
      }
    };
  
    window.addEventListener('resize', handleResize);
    handleResize();
  });
  




  document.addEventListener('DOMContentLoaded', function() {
    var menuIcon = document.getElementById('menu-icon');
    var navbarLinks = document.getElementById('navbar-links');
    var sidebar = document.getElementById('sidebar');

    menuIcon.addEventListener('click', function() {
        navbarLinks.classList.toggle('active');
        sidebar.classList.toggle('active');
    });
});


