<script setup lang="ts">
const imageModules = import.meta.glob(
  '/src/assets/logos/*.{jpg,png,webp}',
  {
    eager: true,
    import: 'default',
  }
)

const images = Object.values(imageModules) as string[]
</script>

<template>
    <div class="map-wrapper">
      <iframe src="https://yandex.by/map-widget/v1/?from=mapframe&indoorLevel=1&ll=27.549992%2C53.869784&mode=search&ol=geo&ouri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgoyMTEzOTUwMzczEjrQkdC10LvQsNGA0YPRgdGMLCDQnNGW0L3RgdC6LCDQv9GA0LDRgdC_0LXQutGCINCc0ZbRgNGDLCAxIgoNY2bcQRWpeldC&source=mapframe&um=constructor%3A%D0%92%D0%90%D0%A8_%D0%9A%D0%9E%D0%94_%D0%9A%D0%90%D0%A0%D0%A2%D0%AB&utm_source=mapframe&z=17.07&theme=dark" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;">
      </iframe>
    </div>
  <footer>
    <div class="container">
      <div class="footer-top">
        <div class="copyright">© All Rights Reserved MaxxCars</div>
        <div class="logos">
          <div v-for="(image, idx) in images" :key="idx">
            <img :src="image" alt="logo" />
          </div>
        </div>
      </div>


    </div>
  </footer>
</template>

<style scoped>
footer {
  width: 100%; 
  height: 120px; 
  display: flex; 
  justify-content: center; 
  align-items: center;
  background-color: black;
  color: white;
  font-family: 'Inter', sans-serif;
}

.container {
  width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 24px;
  align-items: center;
}

.footer-top {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logos {
  display: flex;
  gap: 16px;
}

.logos img {
  width: 24px;
  height: 24px;
  object-fit: contain;
}

.map-wrapper {
    margin-top: 50px;
  width: 100%;
  height: 300px;
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.map-wrapper iframe {
  width: 100%;
  height: 100%;
  border: none;
}
</style>
