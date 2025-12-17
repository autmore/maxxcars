<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { createNewReview, getAllReviews } from '../api/requests'

interface Review {
  name: string
  review: string
  rating: number
}

const reviews = ref<Review[]>([])
const isLoading = ref(false)
const showCreateForm = ref(false)
const hasNextPage = ref(true)
const isCreating = ref(false)
const limit = 3
const offset = ref(0)
const login = ref('')
const review = ref('')
const rating = ref(0)
const maxRating = 5
const hoverRating = ref(0)
const search = ref('')

const setRating = (value: number) => {
  rating.value = value
}

const setHover = (value: number) => {
  hoverRating.value = value
}

const resetHover = () => {
  hoverRating.value = 0
}

const createReview = async () => {
  if (!login.value.trim() || review.value === '') {
    return
  }

  try {
    isCreating.value = true

    const payload = {
      name: login.value.trim(),
      review: review.value,
      rating: rating.value,
    }

    await createNewReview(payload)

    login.value = ''
    review.value = ''
    showCreateForm.value = false

    offset.value = 0
    await fetchReviews()
  } catch (error) {
    console.error(error)
  } finally {
    isCreating.value = false
  }
}

const buildQuery = () => {
  const params = new URLSearchParams()

  if (search.value.trim()) {
    params.append('search', search.value.trim())
  }

  params.append('limit', limit.toString())
  params.append('offset', offset.value.toString())

  return params.toString()
}

const fetchReviews = async (append = false) => {
  try {
    isLoading.value = true
    const query = buildQuery()
    const response = await getAllReviews(`?${query}`)

    if (append) {
      reviews.value.push(...response.results)
    } else {
      reviews.value = response.results
    }

    hasNextPage.value = response.next_page
  } catch (error) {
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

const loadNextPage = () => {
  if (!hasNextPage.value || isLoading.value) return

  offset.value += limit
  fetchReviews(true)
}

onMounted(fetchReviews)

watch(showCreateForm, (value) => {
  document.body.style.overflow = value ? 'hidden' : ''
})

let searchTimeout: number | undefined

watch([search], () => {
  if (searchTimeout) {
    clearTimeout(searchTimeout)
  }

  offset.value = 0

  searchTimeout = window.setTimeout(() => {
    fetchReviews(false)
  }, 400)
})
</script>

<template>
    <img
    alt="background"
    class="background"
    src="../assets/backgrounds/photo-1704475067471-.jpg"
  />
  <div class="review-container">

    <div class="create-section">
  <button class="create-btn" @click="showCreateForm = true">
    Добавить отзыв
  </button>
</div>

<Teleport to="body">
  <div v-if="showCreateForm" class="modal-overlay" @click.self="showCreateForm = false">
    <div class="modal">
      <button class="modal-close" @click="showCreateForm = false">✕</button>

      <h2 class="modal-title">Добавить отзыв</h2>

      <input
        v-model="login"
        type="text"
        placeholder="Логин"
        class="input modal-input"
      />

      <input
        v-model="review"
        type="text"
        placeholder="Отзыв"
        class="input modal-input textarea"
      />

      <div class="rating-stars">
        <span
            v-for="star in maxRating"
            :key="star"
            class="star"
            :class="{ filled: star <= (hoverRating || rating) }"
            @click="setRating(star)"
            @mouseover="setHover(star)"
            @mouseleave="resetHover"
        >★</span>
      </div>


      <button
        class="confirm-btn modal-confirm"
        :disabled="isCreating"
        @click="createReview"
      >
        {{ isCreating ? 'Создание...' : 'Подтвердить' }}
      </button>
    </div>
  </div>
</Teleport>

<div class="filters">
      <input
        v-model="search"
        type="text"
        placeholder="Поиск по имени пользователя и комментарию..."
        class="input search"
      />
    </div>


    <div v-if="isLoading" class="loading">
  Загрузка...
</div>

<div v-else-if="!reviews.length" class="empty">
  Отзывов пока нет
</div>

<div v-else class="reviews">
  <div v-for="(reviewItem, index) in reviews" :key="index" class="review-card">
    <div class="review-header">
      <h2>{{ reviewItem.name }}</h2>
      <div class="rating">
        <span v-for="star in maxRating" :key="star" class="star" :class="{ filled: star <= reviewItem.rating }">★</span>
      </div>
    </div>

    <p class="review-text">
      {{ reviewItem.review }}
    </p>
  </div>
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

.search {
  width: 100%;
}
    .rating-stars {
  display: flex;
  gap: 4px;
  font-size: 24px;
  justify-content: center;
  cursor: pointer;
  margin-bottom: 12px;
}

.star {
  color: #ccc;
  transition: color 0.2s;
}

.star.filled {
  color: #f9a825; 
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

.background {
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  object-fit: cover;
  z-index: -1;
}

.review-container {
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

.reviews {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.review-card {
  background: #fff;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease;
}

.review-card:hover {
  transform: translateY(-4px);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.review-header h2 {
  font-size: 18px;
  margin: 0;
}

.rating {
  display: flex;
  gap: 2px;
  font-weight: 600;
  color: #f9a825;
}

.rating .star {
  font-size: 18px;
  color: #ccc;
}

.rating .star.filled {
  color: #f9a825;
}


.review-text {
  font-size: 14px;
  line-height: 1.5;
  color: #444;
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
</style>
