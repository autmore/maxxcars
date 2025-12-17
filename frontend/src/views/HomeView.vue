<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { createNewOrder, getAllCars } from '../api/requests'

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
const isLoading = ref(false)
const showCreateForm = ref(false)
const hasNextPage = ref(true)
const isCreating = ref(false)
const limit = 3
const offset = ref(0)

const name = ref('')
const phone_number = ref('')
const email = ref('')
const car_id = ref<number | null>(null)

const cars = ref<Car[]>([])

const fetchCars = async () => {
  try {
    const response = await getAllCars(`?limit=20`)
    cars.value = response.results
  } catch (error) {
    console.error(error)
  }
}

const createOrder = async () => {
  if (!name.value.trim() || !phone_number.value.trim() || !email.value.trim() || !car_id.value) return

  try {
    isCreating.value = true
    const payload = {
      name: name.value.trim(),
      phone_number: phone_number.value.trim(),
      email: email.value.trim(),
      car_id: car_id.value
    }
    await createNewOrder(payload)

    name.value = ''
    phone_number.value = ''
    email.value = ''
    car_id.value = null
    showCreateForm.value = false

    offset.value = 0
  } catch (error) {
    console.error(error)
  } finally {
    isCreating.value = false
  }
}

onMounted(() => {
  fetchCars()
})
</script>

<template>
    <img
    alt="background"
    class="background"
    src="../assets/backgrounds/photo-1704475067471-.jpg"
  />
  <div class="home-container">

    <h1>Электромобили для вашего комфорта</h1>
    <h3>Независимо от вашего образа жизни, электромобиль станет надежным и комфортным спутником, делая каждую поездку максимально удобной и приятной.</h3>

    <div class="electro-cars">
        <div class="block">
            <img
                alt=""
                class="block-img"
                src="../assets/photo-1553088558-18a.jpg"
            />
            <h1>Компактный городской электромобиль</h1>
            <h3>Идеально подходит для ежедневных поездок по городу.</h3>
        </div>
        <div class="block">
            <img
                alt=""
                class="block-img"
                src="../assets/photo-1635777076506-.jpg"
            />
            <h1>Электрический кроссовер</h1>
            <h3>Подходит для семейных поездок и путешествий.</h3>
        </div>
        <div class="block">
            <img
                alt=""
                class="block-img"
                src="../assets/photo-1713712150258-.jpg"
            />
            <h1>Электромобиль для бизнеса</h1>
            <h3>Надежный и экономичный выбор для корпоративных клиентов.</h3>
        </div>
        <div class="block">
            <img
                alt=""
                class="block-img"
                src="../assets/photo-1732193998117-.jpg"
            />
            <h1>Электрический минивэн</h1>
            <h3>Просторный и удобный для больших семей и групп.</h3>
        </div>

    </div>

        <div class="create-section">
      <button class="create-btn" @click="showCreateForm = true">
        <h3 style="margin: 0;">Сделать заказ</h3>
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

          <select v-model="car_id" class="input modal-input">
            <option disabled value="">Выберите авто</option>
            <option
              v-for="(car, index) in cars"
              :key="car.id"
              :value="index + 1"
            >
              {{ car.name }} - {{ car.price }} ₽
            </option>
          </select>

          <button class="confirm-btn modal-confirm" :disabled="isCreating" @click="createOrder">
            {{ isCreating ? 'Создание...' : 'Подтвердить' }}
          </button>
        </div>
      </div>
    </Teleport>

    <h1 style="margin-top: 60px;">Контактная информация</h1>
    <h3>Мы рады подобрать для вас идеальный автомобиль, который полностью соответствует вашим потребностям и предпочтениям. Свяжитесь с нами для получения дополнительной информации.</h3>
    

    <div class="contact-info">
        <div class="contact-block">
            <img
                alt=""
                class="contact-img"
                src="../assets/phone_contact_call_ring.svg"
            />
            <h1>Телефон для связи</h1>
            <h3>8 017 123-45-67
maxxcars@example.com</h3>
        </div>
        <div class="contact-block">
            <img
                alt=""
                class="contact-img"
                src="../assets/map_way_mark_where_adress.svg"
            />
            <h1>Наш адрес</h1>
            <h3>г. Минск, проспект Мира, д. 1</h3>
        </div>
        <div class="contact-block">
            <img
                alt=""
                class="contact-img"
                src="../assets/route_map_road.svg"
            />
            <h1>Как нас найти</h1>
            <h3>Пройдите прямо по улице Зелёная до пересечения с ул. Солнечной, поверните налево и пройдите до конца, мы находимся в бизнес-центре 'Эко-парк'.</h3>
        </div>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 24px;
}

.background {
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  object-fit: cover;
  z-index: -1;
  filter: brightness(0.4);
}

h1 {
  font-size: 42px;
  font-weight: 700;
  margin-bottom: 24px;
  text-align: center;
  line-height: 1.2;
  letter-spacing: -0.5px;
}

h3 {
  font-size: 20px;
  font-weight: 400;
  margin-bottom: 48px;
  text-align: center;
  line-height: 1.6;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.electro-cars {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 52px;
  margin-bottom: 80px;
}

.block {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
  border-radius: 24px;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(12px);
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
}

.block::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 24px;
  padding: 1px;
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.2), transparent);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

/* .block:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.04));
  border-color: rgba(255, 255, 255, 0.2);
} */

.block-img {
  width: 500px;
  height: 370px;
  object-fit: cover;
  border-radius: 16px;
  margin-bottom: 24px;
  transition: transform 0.4s ease;
}

/* .block:hover .block-img {
  transform: scale(1.03);
} */

.block h1 {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 12px;
}

.block h3 {
  font-size: 15px;
  margin-bottom: 0;
  line-height: 1.5;
}

.contact-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 32px;
  margin-top: 60px;
  margin-bottom: 80px;
}

.contact-block {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
  border-radius: 24px;
  padding: 32px;
  text-align: center;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
}

.contact-block::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 24px;
  padding: 1px;
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.2), transparent);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

/* .contact-block:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 32px rgba(0, 0, 0, 0.4);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.04));
  border-color: rgba(255, 255, 255, 0.2);
} */

.contact-img {
  width: 72px;
  height: 72px;
  object-fit: contain;
  margin-bottom: 24px;
  filter: brightness(1.2);
}

.contact-block h1 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 12px;
}

.contact-block h3 {
  font-size: 16px;
  margin-bottom: 0;
  line-height: 1.5;
  white-space: pre-line;
}

.create-section {
  display: flex;
  justify-content: center;
  margin-bottom: 24px;
}

.create-btn {
    width: 300px;
    height: 80px;
    font-size: 28px;
  padding: 12px 28px;
  border-radius: 999px;
  border: 1px solid #000;
  background: #000;
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

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 16px;
}

.load-more {
  padding: 12px 28px;
  border-radius: 999px;
  border: 1px solid #000;
  background: transparent;
  cursor: pointer;
}

.load-more:hover:not(:disabled) {
  background: #000;
  color: #fff;
}

.load-more:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>