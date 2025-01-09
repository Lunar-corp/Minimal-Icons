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
    <polyline points="3.5 2 6.5 12.5 18 12.5" />
    <line x1="9.5" x2="5.5" y1="12.5" y2="20" />
    <line x1="15" x2="18.5" y1="12.5" y2="20" />
    <path d="M2.75 18a13 13 0 0 0 18.5 0" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>