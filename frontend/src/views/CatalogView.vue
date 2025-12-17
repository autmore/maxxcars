<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { createNewCar, getAllCars } from '../api/requests'
import router from '../router'

interface Car {
    id: number
  name: string
  price: number
  image?: string
}

const imageModules = import.meta.glob(
  '/src/assets/img/*.{jpg,png,webp}',
  {
    eager: true,
    import: 'default',
  }
)

const images = Object.values(imageModules) as string[]

const cars = ref<Car[]>([])
const isLoading = ref(false)
const limit = 9
const offset = ref(0)
const hasNextPage = ref(true)
const search = ref('')
const priceMin = ref<string>('') 
const priceMax = ref<string>('') 
const showCreateForm = ref(false)
const newCarName = ref('')
const newCarPrice = ref<string>('')
const isCreating = ref(false)

const buildQuery = () => {
  const params = new URLSearchParams()

  if (search.value.trim()) {
    params.append('search', search.value.trim())
  }

  if (priceMin.value !== '' && !isNaN(Number(priceMin.value))) {
    params.append('price_min', priceMin.value)
  }

  if (priceMax.value !== '' && !isNaN(Number(priceMax.value))) {
    params.append('price_max', priceMax.value)
  }

  params.append('limit', limit.toString())
  params.append('offset', offset.value.toString())

  return params.toString()
}

const fetchCars = async (append = false) => {
  try {
    isLoading.value = true

    const query = buildQuery()
    const response = await getAllCars(`?${query}`)

    const mappedCars = response.results.map((car: Car, index: number) => ({
        ...car,
        image: images[(offset.value + index) % images.length],
    }))

    if (append) {
      cars.value.push(...mappedCars)
    } else {
      cars.value = mappedCars
    }

    hasNextPage.value = response.next_page
  } catch (error) {
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

let searchTimeout: number | undefined

watch([priceMin, priceMax, search], () => {
  if (searchTimeout) {
    clearTimeout(searchTimeout)
  }

  offset.value = 0

  searchTimeout = window.setTimeout(() => {
    fetchCars(false)
  }, 400)
})

onMounted(fetchCars)

const loadNextPage = () => {
  if (!hasNextPage.value || isLoading.value) return

  offset.value += limit
  fetchCars(true)
}

const handleNavigate = (car: Car, index: number) => {
  router.push({
    name: 'about',
    params: { id: String(index + 1) }, 
    query: {
      image: car.image,
    },
  })
}

watch(showCreateForm, (value) => {
  document.body.style.overflow = value ? 'hidden' : ''
})
</script>

<template>
  <img
    alt="background"
    class="background"
    src="../assets/backgrounds/background-catalog.jpg"
  />

  <div class="car-container">


    <div class="filters">
      <input
        v-model="search"
        type="text"
        placeholder="Поиск по названию..."
        class="input search"
      />

      <input
        v-model="priceMin"
        type="number"
        placeholder="Цена от"
        class="input"
      />

      <input
        v-model="priceMax"
        type="number"
        placeholder="Цена до"
        class="input"
      />
    </div>

    <div v-if="!cars.length && !isLoading" class="empty">
        Автомобили не найдены
    </div>

    <div class="cars">
        <div v-for="(car, index) in cars" :key="index" class="car-card">
        <img :src="car.image" :alt="car.name" class="car-image" />

        <div class="car-header">
          <h2>{{ car.name }}</h2>
        </div>

        <div class="car-footer">
          <span class="price">{{ car.price }} $</span>
        </div>

        <button class="about" @click="handleNavigate(car, index)">
            Подробнее
        </button>
      </div>
    </div>

    <div v-if="isLoading" class="loading-overlay">
        Обновление...
    </div>

    <div class="pagination" v-if="hasNextPage">
        <button
            class="load-more"
            :disabled="isLoading"
            @click="loadNextPage"
        >
            Загрузить ещё
        </button>
    </div>

  </div>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  position: relative;
  width: 420px;
  padding: 32px;
  background: #fff;
  border-radius: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
  animation: modalIn 0.25s ease;
}

@keyframes modalIn {
  from {
    transform: translateY(20px) scale(0.98);
    opacity: 0;
  }
  to {
    transform: none;
    opacity: 1;
  }
}

.modal-close {
  position: absolute;
  top: 14px;
  right: 14px;
  border: none;
  background: transparent;
  font-size: 18px;
  cursor: pointer;
}

.modal-title {
  margin-bottom: 8px;
  font-size: 20px;
  font-weight: 500;
  text-align: center;
}

.modal-input {
  width: 100%;
}

.modal-confirm {
  margin-top: 12px;
  width: 100%;
}

.create-section {
    width: 100%;
    display: flex;
    justify-content: center;
  margin-bottom: 32px;
}

.create-btn {
  padding: 14px 32px;
  border-radius: 999px;
  border: 1px solid #000;
  background: #000;
  color: #fff;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.25s ease;
}

.create-btn:hover {
  background: #fff;
  color: #000;
}

.create-form {
  margin-top: 20px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 16px;
  display: flex;
  gap: 16px;
  align-items: center;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
}

.confirm-btn {
  padding: 12px 28px;
  border-radius: 999px;
  border: 1px solid #000;
  background: transparent;
  color: #000;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.25s ease;
}

.confirm-btn:hover:not(:disabled) {
  background: #000;
  color: #fff;
}

.confirm-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.background {
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  object-fit: cover;
  z-index: -1;
}

.car-container {
  width: 1200px;
  max-width: 100%;
  margin: 0 auto;
  padding: 24px;
}

.title {
  font-size: 28px;
  margin-bottom: 24px;
}

.loading,
.empty {
  text-align: center;
  font-size: 18px;
  color: #666;
}

.cars {
  display: flex;
  flex-wrap: wrap;
}

.car-card {
  background: #fff;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease;
}

.car-card:hover {
  transform: translateY(-4px);
}

.car-header h2 {
  font-size: 18px;
  margin: 0 0 12px;
}

.car-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  font-size: 16px;
  font-weight: 400;
}

.car-image {
  width: 360px;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 12px;
}

.filters {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
  padding: 16px 20px;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 16px;
  backdrop-filter: blur(6px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
}

.input {
  width: 380px;
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid #ddd;
  background: #fff;
  color: #111;
  font-size: 14px;
  outline: none;
  transition: all 0.25s ease;
}

.search {
  width: 540px;
}

.input::placeholder {
  color: #999;
}

.input:hover {
  border-color: #000;
}

.input:focus {
  border-color: #000;
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.08);
}

.loading-overlay {
  margin-top: 16px;
  font-size: 14px;
  color: #555;
  text-align: center;
  letter-spacing: 0.5px;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 32px;
}

.load-more {
  padding: 14px 32px;
  font-size: 14px;
  border-radius: 999px;
  border: 1px solid #000;
  background: transparent;
  color: #000;
  cursor: pointer;
  transition: all 0.25s ease;
}

.load-more:hover:not(:disabled) {
  background: #000;
  color: #fff;
}

.load-more:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.about {
  margin-top: 32px;
  padding: 14px 32px;
  font-size: 14px;
  border-radius: 999px;
  border: 1px solid #000;
  background: transparent;
  color: #fff;
  background-color: #000;
  cursor: pointer;
  transition: all 0.25s ease;
}

.about:hover:not(:disabled) {
  background: #fff;
  color: #000;
}

.about:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
