<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <rect width="14" height="6" x="5" y="14" rx="2" />
    <rect width="10" height="6" x="7" y="4" rx="2" />
    <path d="M22 7h-5" />
    <path d="M7 7H1" />
    <path d="M22 17h-3" />
    <path d="M5 17H2" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>