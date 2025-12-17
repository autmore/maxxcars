<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { createNewOrder, getOneCar } from '../api/requests'

interface Car {
  id: number
  name: string
  price: number
}

interface Order {
  name: string
  phone_number: string
  email: string
  car: Car
}

const orders = ref<Order[]>([])
const showCreateForm = ref(false)
const isCreating = ref(false)

const name = ref('')
const phone_number = ref('')
const email = ref('')
const cars = ref<Car[]>([])

const route = useRoute()
const router = useRouter()

const car = ref<Car | null>(null)
const isLoading = ref(true)

const carId = route.params.id as string
const image = route.query.image as string

const fetchCar = async () => {
  try {
    const response = await getOneCar(carId)
    car.value = response
  } catch (e) {
    console.error(e)
  } finally {
    isLoading.value = false
  }
}

onMounted(fetchCar)

const closeModal = () => {
  router.back()
}

const createOrder = async () => {
  if (!name.value.trim() || !phone_number.value.trim() || !email.value.trim()) return

  try {
    isCreating.value = true
    const payload = {
      name: name.value.trim(),
      phone_number: phone_number.value.trim(),
      email: email.value.trim(),
      car_id: carId
    }
    await createNewOrder(payload)

    name.value = ''
    phone_number.value = ''
    email.value = ''
    showCreateForm.value = false

  } catch (error) {
    console.error(error)
  } finally {
    isCreating.value = false
  }
}
</script>

<template>
  <div class="modal-main">
    <button class="close" @click="closeModal">✕</button>

    <div v-if="isLoading" class="loading">Загрузка...</div>

    <div v-else class="content">
      <img :src="image" :alt="car?.name" class="image" />

      <div class="info">
        <h1>{{ car?.name }}</h1>
        <p class="price">{{ car?.price }} $</p>

        <div class="create-section">
      <button class="create-btn" @click="showCreateForm = true">
        Сделать заказ
      </button>
    </div>

    <Teleport to="body">
      <div v-if="showCreateForm" class="modal-overlay" @click.self="showCreateForm = false">
        <div class="modal">
          <button class="modal-close" @click="showCreateForm = false">✕</button>
          <h2 class="modal-title">Добавить заказ</h2>

          <input v-model="name" type="text" placeholder="Имя" class="input modal-input" />
          <input v-model="phone_number" type="text" placeholder="Телефон" class="input modal-input" />
          <input v-model="email" type="email" placeholder="Email" class="input modal-input" />

          <button class="confirm-btn modal-confirm" :disabled="isCreating" @click="createOrder">
            {{ isCreating ? 'Создание...' : 'Подтвердить' }}
          </button>
        </div>
      </div>
    </Teleport>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-main {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.95);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close {
  position: absolute;
  top: 24px;
  right: 24px;
  font-size: 28px;
  color: white;
  background: none;
  border: none;
  cursor: pointer;
}

.content {
  display: flex;
  gap: 48px;
  max-width: 1200px;
  width: 100%;
  padding: 40px;
}

.image {
  width: 60%;
  height: 420px;
  object-fit: cover;
  border-radius: 16px;
}

.info {
  color: white;
}

.info h1 {
  font-size: 36px;
  margin-bottom: 16px;
}

.price {
  font-size: 24px;
  opacity: 0.8;
}

.create-section {
  display: flex;
  justify-content: center;
  margin-bottom: 24px;
}

.create-btn {
  padding: 12px 28px;
  border-radius: 999px;
  border: 1px solid #000;
  background: #000;
  color: #fff;
  cursor: pointer;
}

.create-btn:hover {
  background: #fff;
  color: #000;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 3000;
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
  border: 1px solid #fff;
  background: #fff;
  color: #000;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.25s ease;
}

.create-btn:hover {
  background: #000;
  color: #fff;
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

.input {
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid #ddd;
  background: #fff;
  color: #111;
  font-size: 14px;
  outline: none;
  transition: all 0.25s ease;
}
</style>
