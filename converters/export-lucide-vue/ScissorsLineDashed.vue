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
    <path d="M5.42 9.42 8 12" />
    <circle cx="4" cy="8" r="2" />
    <path d="m14 6-8.58 8.58" />
    <circle cx="4" cy="16" r="2" />
    <path d="M10.8 14.8 14 18" />
    <path d="M16 12h-2" />
    <path d="M22 12h-2" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>