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
    <circle cx="6" cy="6" r="3" />
    <path d="M6 9v12" />
    <path d="m21 3-6 6" />
    <path d="m21 9-6-6" />
    <path d="M18 11.5V15" />
    <circle cx="18" cy="18" r="3" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>