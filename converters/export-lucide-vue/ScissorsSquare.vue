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
    <rect width="20" height="20" x="2" y="2" rx="2" />
    <circle cx="8" cy="8" r="2" />
    <path d="M9.414 9.414 12 12" />
    <path d="M14.8 14.8 18 18" />
    <circle cx="8" cy="16" r="2" />
    <path d="m18 6-8.586 8.586" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>