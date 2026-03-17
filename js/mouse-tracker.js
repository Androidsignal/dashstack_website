// Mouse Tracker Effect
(function() {
  // Check if elements exist
  const mouseLight = document.getElementById('mouseLight');
  const mouseLightInner = document.getElementById('mouseLightInner');
  const mouseRing = document.getElementById('mouseRing');

  if (!mouseLight || !mouseLightInner || !mouseRing) {
    return;
  }

  let lightX = 0, lightY = 0;
  let innerX = 0, innerY = 0;
  let ringX = 0, ringY = 0;
  let targetX = 0, targetY = 0;

  document.addEventListener('mousemove', (e) => {
    targetX = e.clientX;
    targetY = e.clientY;
  });

  function animate() {
    // Smooth follow with different speeds for layered effect
    lightX += (targetX - lightX) * 0.08;
    lightY += (targetY - lightY) * 0.08;
    
    innerX += (targetX - innerX) * 0.15;
    innerY += (targetY - innerY) * 0.15;
    
    ringX += (targetX - ringX) * 0.25;
    ringY += (targetY - ringY) * 0.25;

    mouseLight.style.left = lightX + 'px';
    mouseLight.style.top = lightY + 'px';
    
    mouseLightInner.style.left = innerX + 'px';
    mouseLightInner.style.top = innerY + 'px';
    
    mouseRing.style.left = ringX + 'px';
    mouseRing.style.top = ringY + 'px';

    requestAnimationFrame(animate);
  }

  animate();

  // Click effect - expand ring briefly
  document.addEventListener('click', () => {
    mouseRing.style.width = '80px';
    mouseRing.style.height = '80px';
    setTimeout(() => {
      mouseRing.style.width = '60px';
      mouseRing.style.height = '60px';
    }, 200);
  });
})();
