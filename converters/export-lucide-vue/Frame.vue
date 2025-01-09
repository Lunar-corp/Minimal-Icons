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
    <line x1="22" x2="2" y1="6" y2="6" />
    <line x1="22" x2="2" y1="18" y2="18" />
    <line x1="6" x2="6" y1="2" y2="22" />
    <line x1="18" x2="18" y1="2" y2="22" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>