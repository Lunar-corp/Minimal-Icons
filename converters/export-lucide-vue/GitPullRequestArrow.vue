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
    <circle cx="5" cy="6" r="3" />
    <path d="M5 9v12" />
    <circle cx="19" cy="18" r="3" />
    <path d="m15 9-3-3 3-3" />
    <path d="M12 6h5a2 2 0 0 1 2 2v7" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>