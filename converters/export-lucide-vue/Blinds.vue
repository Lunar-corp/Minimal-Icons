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
    <path d="M3 3h18" />
    <path d="M20 7H8" />
    <path d="M20 11H8" />
    <path d="M10 19h10" />
    <path d="M8 15h12" />
    <path d="M4 3v14" />
    <circle cx="4" cy="19" r="2" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>