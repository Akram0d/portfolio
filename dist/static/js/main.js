(function () {
  // Theme toggle
  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  // Project filters
  var chips = document.querySelectorAll('.chip');
  var projects = document.querySelectorAll('.project');
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var f = chip.dataset.filter;
      chips.forEach(function (c) { c.classList.toggle('active', c === chip); });
      projects.forEach(function (p) {
        p.hidden = f !== 'all' && p.dataset.tags.split(' ').indexOf(f) === -1;
      });
    });
  });

  // Demo video dialog
  var dialog = document.getElementById('video-dialog');
  if (dialog) {
    var video = document.getElementById('demo-video');
    var title = document.getElementById('video-title');
    document.querySelectorAll('[data-video]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        video.src = btn.dataset.video;
        title.textContent = btn.dataset.title;
        dialog.showModal();
        video.play();
      });
    });
    dialog.addEventListener('close', function () {
      video.pause();
      video.removeAttribute('src');
      video.load();
    });
    dialog.addEventListener('click', function (e) { if (e.target === dialog) dialog.close(); });
  }
})();
